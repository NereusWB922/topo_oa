import json
import pandas as pd
import tabula as tb


class DataIngestor:
    def ingest_from_json(self, file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
        return data

    def ingest_from_csv(self, file_path):
        df = pd.read_csv(file_path)
        return df.to_dict(orient="records")

    def ingest_from_pdf(self, file_path):
        df = tb.read_pdf(file_path, pages="1", multiple_tables=False)
        return df[0].to_dict(orient="records")
