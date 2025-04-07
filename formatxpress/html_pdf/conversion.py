from pdfkit import from_file
from utils.conversions import Conversions


class HtmlPdfConversions(Conversions):
    def html2pdf(self, html_path: str, id: int):
        from_file(html_path, f"{self.path}{id}.pdf")
        with open(f"{self.path}{id}.pdf", "rb") as f:
            return f.read()
