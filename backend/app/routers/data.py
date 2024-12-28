from fastapi import APIRouter
from app.pipeline.pipeline import Pipeline
from app.pipeline.ingestion.csv_ingestion import CsvIngestion
from app.pipeline.ingestion.json_ingestion import JsonIngestion
from app.pipeline.ingestion.pdf_ingestion import PdfIngestion
from app.pipeline.ingestion.pptx_ingestion import PptxIngestion
from app.pipeline.processing.key_formatter import KeyFormatter
from app.pipeline.processing.parse_str_to_num import ParseStrToNum
from app.pipeline.processing.process_adhoc_pptx import ProcessAdhocPptx

router = APIRouter(prefix="/api/data")

dummy_data = [
    {"name": "Item 1", "value": 100},
    {"name": "Item 2", "value": 200},
    {"name": "Item 3", "value": 300},
]


@router.get("")
def get_full_data():
    return dummy_data


@router.get("/{file_type}")
def get_data_by_type(file_type: str):
    if file_type == "json":
        return (
            Pipeline()
            .add_step(JsonIngestion("app/datasets/dataset1.json"))
            .add_step(KeyFormatter())
            .execute()
        )
    elif file_type == "csv":
        return (
            Pipeline()
            .add_step(CsvIngestion("app/datasets/dataset2.csv"))
            .add_step(KeyFormatter())
            .execute()
        )
    elif file_type == "pdf":
        return (
            Pipeline()
            .add_step(PdfIngestion("app/datasets/dataset3.pdf"))
            .add_step(KeyFormatter())
            .add_step(ParseStrToNum(target_fields=["revenue_in_$"]))
            .execute()
        )
    elif file_type == "pptx":
        return (
            Pipeline()
            .add_step(PptxIngestion("app/datasets/dataset4.pptx"))
            .add_step(ProcessAdhocPptx())
            .add_step(KeyFormatter())
            .add_step(
                ParseStrToNum(
                    target_fields=[
                        "key_highlights.total_revenue",
                        "key_highlights.total_memberships_sold",
                        "quarterly_metrics.revenue_in_$",
                        "quarterly_metrics.memberships_sold",
                        "quarterly_metrics.avg_duration_minutes",
                        "revenue_distribution.gym",
                        "revenue_distribution.pool",
                        "revenue_distribution.tennis_court",
                        "revenue_distribution.personal_training",
                    ]
                )
            )
            .execute()
        )
    else:
        supported_types = ["json", "csv", "pdf", "pptx"]
        raise ValueError(
            f"Unsupported file type: {file_type}. Supported file types are: {', '.join(supported_types)}"
        )
