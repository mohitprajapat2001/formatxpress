from rest_framework.serializers import ModelSerializer, ValidationError
from utils.utils import get_model
from utils.constants import AppModelNames, ValidContentType, ValidationErrors

Pdf2Image = get_model(**AppModelNames.Pdf2Image)
PdfImages = get_model(**AppModelNames.PdfImages)


class PdfImagesSerializer(ModelSerializer):
    class Meta:
        model = PdfImages
        fields = ["image"]


class Pdf2ImageSerializer(ModelSerializer):
    images = PdfImagesSerializer(many=True, read_only=True)

    class Meta:
        model = Pdf2Image
        fields = ["pdf", "images", "user"]
        read_only_fields = ["user"]

    def validate_pdf(self, value):
        if value.content_type != ValidContentType.PDF:
            raise ValidationError(ValidationErrors.ContentTypeError)
        return value

    # def create(self, validated_data):
    #     instance = super().create(validated_data)
    #     try:
    #         pass
    #     except Exception as err:
    #         raise ValidationError(f"Error converting pdf to image: {err}")
