from utils.utils import get_model
from utils.constants import AppModelNames

Pdf2Image = get_model(**AppModelNames.Pdf2Image)
PdfImages = get_model(**AppModelNames.PdfImages)
