from fastapi import APIRouter
from app.services.data_provider import DataProvider

router = APIRouter(prefix="/api/data")

dataProvider = DataProvider()


@router.get("")
def get_full_data():
    return dataProvider.get_full_data()


@router.get("/{file_type}")
def get_data_by_file_type(file_type: str):
    return dataProvider.get_data_by_file_type(file_type)
