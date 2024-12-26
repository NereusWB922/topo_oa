from fastapi import APIRouter
from app.services.data_ingestor import DataIngestor

router = APIRouter(prefix="/api/data")
data_ingestor = DataIngestor()

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
        return data_ingestor.ingest_from_json("app/datasets/dataset1.json")
    elif file_type == "csv":
        return data_ingestor.ingest_from_csv("app/datasets/dataset2.csv")
    else:
        supported_types = ["json", "csv"]
        raise ValueError(
            f"Unsupported file type: {file_type}. Supported file types are: {', '.join(supported_types)}"
        )
