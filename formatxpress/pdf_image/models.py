from utils.models import UserFieldAbstractModel
from django.db import models
from pdf_image.constants import UploadPaths


class Pdf2Image(UserFieldAbstractModel):
    pdf = models.FileField(upload_to=UploadPaths.PDF_PATH)

    def __str__(self):
        return self.pdf.name


class PdfImages(models.Model):
    pdf = models.ForeignKey(Pdf2Image, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to=UploadPaths.IMAGES_PATH)

    def __str__(self):
        return self.image.name
