from fastapi import APIRouter
from app.services.data_provider import DataProvider

router = APIRouter(prefix="/api/data")

dummy_data = [
    {"name": "Item 1", "value": 100},
    {"name": "Item 2", "value": 200},
    {"name": "Item 3", "value": 300},
]


@router.get("")
def get_full_data():
    return dummy_data
