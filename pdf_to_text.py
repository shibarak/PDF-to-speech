import sys
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
import io


class Pdf:
    def __init__(self):
        self.rsrcmgr = PDFResourceManager()
        self.retstr = io.StringIO()
        self.laparams = LAParams()
        self.device = TextConverter(self.rsrcmgr, self.retstr, laparams=self.laparams)
        self.interpreter = PDFPageInterpreter(self.rsrcmgr, self.device)
        # Create a PDF interpreter object.

        # Process each page contained in the document.
        self.pdf_data = ""
        self.text = ""

    #  Converts PDF to a string.
    def pdftt(self):
        fp = open(self.pdf_data, 'rb')
        for page in PDFPage.get_pages(fp):
            self.interpreter.process_page(page)
            self.text = self.retstr.getvalue()
        self.reset()

    # Resets the parser so it's clear for the next PDF
    def reset(self):
        self.rsrcmgr = PDFResourceManager()
        self.retstr = io.StringIO()
        self.laparams = LAParams()
        self.device = TextConverter(self.rsrcmgr, self.retstr, laparams=self.laparams)
        self.interpreter = PDFPageInterpreter(self.rsrcmgr, self.device)