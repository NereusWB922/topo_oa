import json
from app.pipeline.step import Step


class JsonIngestion(Step):
    def __init__(self, file_path):
        self.file_path = file_path

    def execute(self, data={}):
        with open(self.file_path, "r") as file:
            result = json.load(file)
        return result
