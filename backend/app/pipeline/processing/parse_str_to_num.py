from typing import List
from decimal import Decimal, InvalidOperation
from app.pipeline.step import Step


class ParseStrToNum(Step):
    def __init__(self, target_fields: List[str] = None):
        self.target_fields = target_fields if target_fields is not None else []

    def execute(self, data):
        return self.__transform__(data)

    def __should_parse_field__(self, full_path: str) -> bool:
        return full_path in self.target_fields

    def __parse_str_to_num__(self, value: str):
        if value is None:
            return None
        try:
            number = Decimal(value.replace(",", ""))
            return int(number) if number % 1 == 0 else float(number)
        except InvalidOperation:
            return value

    def __transform__(self, data, parent_path: str = ""):
        if isinstance(data, dict):
            return {
                key: (self.__transform__(value, f"{parent_path}.{key}".strip(".")))
                for key, value in data.items()
            }
        elif isinstance(data, list):
            return [self.__transform__(item, parent_path) for item in data]
        else:
            return (
                self.__parse_str_to_num__(data)
                if self.__should_parse_field__(parent_path)
                else data
            )
