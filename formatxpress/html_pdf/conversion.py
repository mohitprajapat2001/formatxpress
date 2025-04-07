from pdfkit import from_file
from utils.conversions import Conversions


class HtmlPdfConversions(Conversions):
    """HTML PDF Conversions Base Class"""

    def html2pdf(self, html_path: str, id: int):
        """Convert HTML to PDF"""
        from_file(html_path, f"{self.path}{id}.pdf")
        with open(f"{self.path}{id}.pdf", "rb") as f:
            return f.read()

    def pdf2html(self, pdf_path: str, id: int):
        """Convert PDF to HTML"""
        pass
