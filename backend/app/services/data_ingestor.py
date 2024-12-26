import json
import pandas as pd


class DataIngestor:
    def ingest_from_json(self, file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
        return data

    def ingest_from_csv(self, file_path):
        df = pd.read_csv(file_path)
        return df.to_dict(orient="records")
