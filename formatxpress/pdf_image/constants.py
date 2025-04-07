from django.utils.translation import gettext_lazy as _


class UploadPaths:
    """Default upload path for html-pdf conversion"""

    PDF_PATH = "pdf_image/pdf/"
    IMAGES_PATH = "pdf_image/images/"


class ValidationErrors:
    """HTML PDF Validation Errors"""

    ContentTypeError = _("Invalid Content Type")
