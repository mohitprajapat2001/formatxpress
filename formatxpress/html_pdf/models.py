from django.db import models
from utils.models import UserFieldAbstractModel
from html_pdf.constants import UploadPaths


class HtmlPdf(UserFieldAbstractModel):
    html = models.FileField(upload_to=UploadPaths.HTML_PATH, null=True, blank=True)
    pdf = models.FileField(upload_to=UploadPaths.PDF_PATH, null=True, blank=True)

    def __str__(self):
        return "HTML %s 2 PDF %s" % (self.html.name, self.pdf.name)
