from django.contrib.admin import register, ModelAdmin
from html_pdf.models import HtmlPdf


@register(HtmlPdf)
class HtmlPdfAdmin(ModelAdmin):
    pass
