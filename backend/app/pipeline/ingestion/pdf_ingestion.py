from app.pipeline.step import Step
import tabula as tb


class PdfIngestion(Step):
    def __init__(self, file_path):
        self.file_path = file_path

    def execute(self, data={}):
        df = tb.read_pdf(self.file_path)
        return df[0].to_dict(orient="records")
