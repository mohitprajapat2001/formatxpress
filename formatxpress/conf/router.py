from rest_framework.routers import DefaultRouter
from html_pdf.api.api import HtmlPdfViewSet

router = DefaultRouter()
router.trailing_slash = "/"
# HTML PDF Conversion
router.register("htmlpdf", HtmlPdfViewSet, basename="htmlpdf")
