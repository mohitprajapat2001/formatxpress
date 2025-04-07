from utils.utils import get_model
from utils.constants import AppModelNames, ValidContentType
from rest_framework.serializers import (
    ModelSerializer,
    ValidationError,
)
from html_pdf.constants import ValidationErrors, PdfHtmlFixturePath
from django.core.files.base import ContentFile
from html_pdf.conversion import HtmlPdfConversions


HtmlPdf = get_model(**AppModelNames.HtmlPdf)


class HtmlPdfSerializer(ModelSerializer):
    class Meta:
        model = HtmlPdf
        fields = ("id", "html", "pdf", "user", "created", "modified")
        read_only_fields = ("id", "user", "created", "modified")

    def validate(self, attrs):
        if not (attrs["pdf"] or attrs["html"]):
            raise ValidationError("Please provide either html or pdf file")
        return super().validate(attrs)

    def validate_pdf(self, value):
        if not value:
            return value
        if value.content_type != ValidContentType.PDF:
            raise ValidationErrors(ValidationErrors.ContentTypeError)
        return value

    def validate_html(self, value):
        if not value:
            return value
        if value.content_type != ValidContentType.HTML:
            raise ValidationErrors(ValidationErrors.ContentTypeError)
        return value

    def create(self, validated_data):
        instance = super().create(validated_data)
        try:
            if not validated_data["pdf"]:
                # If !PDF use Pdfkit and instance.html to convert HTML -> PDF
                name = validated_data["html"].name.split(".")[0]
                convert_obj = HtmlPdfConversions(
                    path=PdfHtmlFixturePath,
                    name=name,
                )
                pdf_content = convert_obj.html2pdf(
                    html_path=instance.html.path, id=instance.id
                )
                instance.pdf.save(f"{name}.pdf", ContentFile(pdf_content))
            elif not validated_data["html"]:
                # if !HTML use pdfkit and instance.pdf to convert PDF -> HTML
                pass
            return instance
        except Exception as e:
            instance.delete()
            raise ValidationError(f"Error converting html to pdf: {e}")
