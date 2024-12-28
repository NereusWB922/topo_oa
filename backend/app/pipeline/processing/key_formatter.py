import re
from app.pipeline import Step


class KeyFormatter(Step):
    def execute(self, data):
        return self.__transform__(data)

    def __to_snake_case__(self, key: str) -> str:
        key = re.sub(r"[()]", " ", key)
        key = key.strip()
        key = re.sub(r"\s+", "_", key)
        return key.lower()

    def __transform__(self, data):
        if isinstance(data, dict):
            return {
                self.__to_snake_case__(key): self.__transform__(value)
                for key, value in data.items()
            }
        elif isinstance(data, list):
            return [self.__transform__(item) for item in data]
        else:
            return data
