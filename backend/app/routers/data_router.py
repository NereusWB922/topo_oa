from fastapi import APIRouter
from app.services.data_provider import DataProvider
from fastapi import HTTPException

router = APIRouter(prefix="/api/data")

dataProvider = DataProvider()


@router.get("")
def get_full_data():
    return dataProvider.get_full_data()


@router.get("/{file_type}")
def get_data_by_file_type(file_type: str):
    try:
        return dataProvider.get_data_by_file_type(file_type)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
