from app.pipeline.ingestion import PdfIngestion


def test_execute():
    expected_result = [
        {"id": 1, "name": "John Doe", "age": 28, "city": "New York"},
        {"id": 2, "name": "Jane Smith", "age": 34, "city": "Los Angeles"},
        {"id": 3, "name": "Emily Johnson", "age": 22, "city": "Chicago"},
    ]

    result = PdfIngestion("tests/test_datasets/pdf_dataset.pdf").execute()

    assert result == expected_result
