from math import exp
import pytest
from app.services.data_ingestor import DataIngestor


@pytest.fixture
def data_ingestor():
    return DataIngestor()


@pytest.fixture
def expected_result():
    return [
        {"id": 1, "name": "John Doe", "age": 28, "city": "New York"},
        {"id": 2, "name": "Jane Smith", "age": 34, "city": "Los Angeles"},
        {"id": 3, "name": "Emily Johnson", "age": 22, "city": "Chicago"},
    ]


def test_ingest_csv_file(data_ingestor: DataIngestor, expected_result):
    result = data_ingestor.ingest_from_csv(
        "tests/test_services/test_datasets/csv_dataset.csv"
    )

    assert result == expected_result


def test_ingest_json_file(data_ingestor: DataIngestor, expected_result):
    result = data_ingestor.ingest_from_json(
        "tests/test_services/test_datasets/json_dataset.json"
    )

    assert result == expected_result


def test_ingest_pdf_file(data_ingestor: DataIngestor, expected_result):
    result = data_ingestor.ingest_from_pdf(
        "tests/test_services/test_datasets/pdf_dataset.pdf"
    )

    assert result == expected_result
