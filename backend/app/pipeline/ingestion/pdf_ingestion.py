from app.pipeline import Step
import pdfplumber
import pandas as pd


class PdfIngestion(Step):
    def __init__(self, file_path):
        self.file_path = file_path

    def execute(self, data={}):
        with pdfplumber.open(self.file_path) as pdf:
            tables = pdf.pages[0].extract_tables()
        df = pd.DataFrame(tables[0][1:], columns=tables[0][0])
        return df.to_dict(orient="records")
