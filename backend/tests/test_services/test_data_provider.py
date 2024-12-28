import pytest
from app.services.data_provider import DataProvider


@pytest.fixture
def mock_pipeline(mocker):
    mock_pipeline = mocker.patch("app.services.data_provider.Pipeline")
    mock_pipeline.return_value.execute.side_effect = [
        {"json_data": "data"},
        {"csv_data": "data"},
        {"pdf_data": "data"},
        {"pptx_data": "data"},
    ]
    return mock_pipeline


def test_get_full_data(mock_pipeline):
    data_provider = DataProvider()
    full_data = data_provider.get_full_data()
    assert full_data == {
        "json": {"json_data": "data"},
        "csv": {"csv_data": "data"},
        "pdf": {"pdf_data": "data"},
        "pptx": {"pptx_data": "data"},
    }


def test_get_data_by_file_type(mock_pipeline):
    data_provider = DataProvider()

    json_data = data_provider.get_data_by_file_type("json")
    assert json_data == {"json_data": "data"}

    csv_data = data_provider.get_data_by_file_type("csv")
    assert csv_data == {"csv_data": "data"}

    pdf_data = data_provider.get_data_by_file_type("pdf")
    assert pdf_data == {"pdf_data": "data"}

    pptx_data = data_provider.get_data_by_file_type("pptx")
    assert pptx_data == {"pptx_data": "data"}


def test_get_data_by_file_type_invalid():
    data_provider = DataProvider()
    with pytest.raises(ValueError) as excinfo:
        data_provider.get_data_by_file_type("txt")
    assert "Supported file types are: json, csv, pdf, pptx" in str(excinfo.value)
