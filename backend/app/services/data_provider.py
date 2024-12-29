from app.pipeline import Pipeline
from app.pipeline.ingestion import (
    CsvIngestion,
    JsonIngestion,
    PdfIngestion,
    PptxIngestion,
)
from app.pipeline.processing import KeyFormatter, ParseStrToNum, ProcessAdhocPptx


class DataProvider:
    def __init__(self):
        self._supported_types = ["json", "csv", "pdf", "pptx"]
        self._data = {}

        self._data["json"] = Pipeline(
            [JsonIngestion("app/datasets/dataset1.json"), KeyFormatter()]
        ).execute()

        self._data["csv"] = Pipeline(
            [CsvIngestion("app/datasets/dataset2.csv"), KeyFormatter()]
        ).execute()

        self._data["pdf"] = Pipeline(
            [
                PdfIngestion("app/datasets/dataset3.pdf"),
                KeyFormatter(),
                ParseStrToNum(
                    target_fields=[
                        "year",
                        "memberships_sold",
                        "revenue_in_$",
                        "avg_duration_minutes",
                    ]
                ),
            ]
        ).execute()

        self._data["pptx"] = Pipeline(
            [
                PptxIngestion("app/datasets/dataset4.pptx"),
                ProcessAdhocPptx(),
                KeyFormatter(),
                ParseStrToNum(
                    target_fields=[
                        "key_highlights.total_revenue",
                        "key_highlights.total_memberships_sold",
                        "quarterly_metrics.revenue_in_$",
                        "quarterly_metrics.memberships_sold",
                        "revenue_distribution.gym",
                        "revenue_distribution.pool",
                        "revenue_distribution.tennis_court",
                        "revenue_distribution.personal_training",
                    ]
                ),
            ]
        ).execute()

    def get_full_data(self):
        return self._data

    def get_data_by_file_type(self, file_type):
        if file_type not in self._supported_types:
            raise ValueError(
                f"Supported file types are: {', '.join(self._supported_types)}"
            )

        return self._data[file_type]
