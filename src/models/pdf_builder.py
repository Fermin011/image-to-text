from PyPDF2 import PdfWriter, PdfReader
import io


class PdfBuilder:
    def __init__(self):
        self._pages = {}

    def add_page(self, index, pdf_bytes):
        self._pages[index] = pdf_bytes

    def clear(self):
        self._pages.clear()

    def build(self, output_path):
        writer = PdfWriter()
        for i in sorted(self._pages.keys()):
            reader = PdfReader(io.BytesIO(self._pages[i]))
            for page in reader.pages:
                writer.add_page(page)
        with open(output_path, "wb") as f:
            writer.write(f)
        self._pages.clear()
        return output_path

    @property
    def page_count(self):
        return len(self._pages)
