from app.pipeline.step import Step
import pandas as pd


class CsvIngestion(Step):
    def __init__(self, file_path):
        self.file_path = file_path

    def execute(self, data={}):
        df = pd.read_csv(self.file_path)
        return df.to_dict(orient="records")
