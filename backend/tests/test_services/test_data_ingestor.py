import pytest
from app.services.data_ingestor import DataIngestor


@pytest.fixture
def data_ingestor():
    return DataIngestor()


def test_ingest_csv_file(data_ingestor: DataIngestor):
    expected_result = [
        {"id": 1, "name": "John Doe", "age": 28, "city": "New York"},
        {"id": 2, "name": "Jane Smith", "age": 34, "city": "Los Angeles"},
        {"id": 3, "name": "Emily Johnson", "age": 22, "city": "Chicago"},
        {"id": 4, "name": "Michael Brown", "age": 45, "city": "Houston"},
        {"id": 5, "name": "Jessica Davis", "age": 30, "city": "Phoenix"},
    ]

    result = data_ingestor.ingest_from_csv(
        "tests/test_services/test_datasets/csv_dataset.csv"
    )

    assert result == expected_result


def test_ingest_json_file(data_ingestor: DataIngestor):
    expected_result = [
        {"id": 1, "name": "John Doe", "age": 30, "city": "New York"},
        {"id": 2, "name": "Jane Smith", "age": 25, "city": "Los Angeles"},
        {"id": 3, "name": "Emily Johnson", "age": 35, "city": "Chicago"},
    ]

    result = data_ingestor.ingest_from_json(
        "tests/test_services/test_datasets/json_dataset.json"
    )

    assert result == expected_result
