from django.contrib.admin import register, ModelAdmin, StackedInline
from utils.utils import get_model
from utils.constants import AppModelNames

Pdf2Image = get_model(**AppModelNames.Pdf2Image)
PdfImages = get_model(**AppModelNames.PdfImages)


class Pdf2ImageAdmin(StackedInline):
    model = Pdf2Image
    extra = 1


@register(Pdf2Image)
class Pdf2ImageAdmin(ModelAdmin):
    inlines = [Pdf2ImageAdmin]
