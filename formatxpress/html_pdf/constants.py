from django.utils.translation import gettext_lazy as _
from django.conf import settings
from os.path import join

PdfHtmlFixturePath = join(settings.BASE_DIR, "fixtures/html_pdf/")


class UploadPaths:
    """Default upload path for html-pdf conversion"""

    HTML_PATH = "htmlpdf/html/"
    PDF_PATH = "htmlpdf/pdf/"


class ValidationErrors:
    """HTML PDF Validation Errors"""

    ContentTypeError = (_("Invalid Content Type"),)
