from app.pipeline.ingestion.pptx_ingestion import PptxIngestion


def test_execute():
    expected_result = [
        {"texts": ["title", "subtitle"], "tables": []},
        {
            "texts": ["slide with table"],
            "tables": [
                [
                    {"id": "1", "name": "John Doe", "age": "28", "city": "New York"},
                    {
                        "id": "2",
                        "name": "Jane Smith",
                        "age": "34",
                        "city": "Los Angeles",
                    },
                    {
                        "id": "3",
                        "name": "Emily Johnson",
                        "age": "22",
                        "city": "Chicago",
                    },
                ]
            ],
        },
    ]

    result = PptxIngestion("tests/test_datasets/pptx_dataset.pptx").execute()

    assert result == expected_result
