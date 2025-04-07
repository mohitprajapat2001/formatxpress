from rest_framework.viewsets import ModelViewSet
from html_pdf.api.serializers import HtmlPdfSerializer
from utils.utils import get_model
from utils.constants import AppModelNames

HtmlPdf = get_model(**AppModelNames.HtmlPdf)


class HtmlPdfViewSet(ModelViewSet):
    queryset = HtmlPdf.objects.all()
    serializer_class = HtmlPdfSerializer
