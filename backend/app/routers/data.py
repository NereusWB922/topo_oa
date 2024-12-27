from fastapi import APIRouter
from app.pipeline.pipeline import Pipeline
from app.pipeline.ingestion.csv_ingestion import CsvIngestion
from app.pipeline.ingestion.json_ingestion import JsonIngestion
from app.pipeline.ingestion.pdf_ingestion import PdfIngestion
from app.pipeline.ingestion.pptx_ingestion import PptxIngestion

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
            Pipeline().add_step(JsonIngestion("app/datasets/dataset1.json")).execute()
        )
    elif file_type == "csv":
        return Pipeline().add_step(CsvIngestion("app/datasets/dataset2.csv")).execute()
    elif file_type == "pdf":
        return Pipeline().add_step(PdfIngestion("app/datasets/dataset3.pdf")).execute()
    else:
        supported_types = ["json", "csv"]
        raise ValueError(
            f"Unsupported file type: {file_type}. Supported file types are: {', '.join(supported_types)}"
        )
