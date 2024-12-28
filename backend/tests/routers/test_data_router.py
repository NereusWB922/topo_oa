import pytest
from fastapi.testclient import TestClient
from app.routers.data_router import router
from fastapi import FastAPI

app = FastAPI()
app.include_router(router)
client = TestClient(app)


@pytest.fixture
def setup(mocker):
    mocker.patch(
        "app.routers.data_router.DataProvider.get_full_data",
        return_value={
            "json": {"json_data": "data"},
            "csv": {"csv_data": "data"},
            "pdf": {"pdf_data": "data"},
            "pptx": {"pptx_data": "data"},
        },
    )
    mocker.patch(
        "app.routers.data_router.DataProvider.get_data_by_file_type",
        side_effect=lambda file_type: {
            "json": {"json_data": "data"},
            "csv": {"csv_data": "data"},
            "pdf": {"pdf_data": "data"},
            "pptx": {"pptx_data": "data"},
        }.get(file_type),
    )


def test_get_full_data(setup):
    response = client.get("/api/data")
    assert response.status_code == 200
    assert response.json() == {
        "json": {"json_data": "data"},
        "csv": {"csv_data": "data"},
        "pdf": {"pdf_data": "data"},
        "pptx": {"pptx_data": "data"},
    }


def test_get_data_by_file_type(setup):
    response = client.get("/api/data/json")
    assert response.status_code == 200
    assert response.json() == {"json_data": "data"}

    response = client.get("/api/data/csv")
    assert response.status_code == 200
    assert response.json() == {"csv_data": "data"}

    response = client.get("/api/data/pdf")
    assert response.status_code == 200
    assert response.json() == {"pdf_data": "data"}

    response = client.get("/api/data/pptx")
    assert response.status_code == 200
    assert response.json() == {"pptx_data": "data"}


def test_get_data_by_file_type_invalid():
    response = client.get("/api/data/txt")
    assert response.status_code == 400
    assert "Supported file types are: json, csv, pdf, pptx" in response.text
