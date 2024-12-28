import pytest
from app.pipeline.processing import ProcessAdhocPptx


@pytest.fixture
def input():
    return [
        {
            "texts": [
                "FitPro: Annual Summary 2023",
                "Key Highlights:\nTotal Revenue: $10,400,000\nTotal Memberships Sold: 1,520\nTop Location: Downtown",
            ],
            "tables": [],
        },
        {
            "texts": ["Quarterly Metrics"],
            "tables": [
                [
                    {
                        "Quarter": "Q1",
                        "Revenue (in $)": "2,300,000",
                        "Memberships Sold": "320",
                        "Avg Duration (Minutes)": "90",
                    },
                    {
                        "Quarter": "Q2",
                        "Revenue (in $)": "2,500,000",
                        "Memberships Sold": "400",
                        "Avg Duration (Minutes)": "95",
                    },
                ]
            ],
        },
        {
            "texts": [
                "Revenue Breakdown by Activity",
                "Revenue Distribution:\nGym: 40%\nPool: 25%\nTennis Court: 15%\nPersonal Training: 20%",
            ],
            "tables": [],
        },
    ]


@pytest.fixture
def expected_result():
    return {
        "Key Highlights": {
            "Total Revenue": "$10,400,000",
            "Total Memberships Sold": "1,520",
            "Top Location": "Downtown",
        },
        "Quarterly Metrics": [
            {
                "Quarter": "Q1",
                "Revenue (in $)": "2,300,000",
                "Memberships Sold": "320",
                "Avg Duration (Minutes)": "90",
            },
            {
                "Quarter": "Q2",
                "Revenue (in $)": "2,500,000",
                "Memberships Sold": "400",
                "Avg Duration (Minutes)": "95",
            },
        ],
        "Revenue Distribution": {
            "Gym": "40%",
            "Pool": "25%",
            "Tennis Court": "15%",
            "Personal Training": "20%",
        },
    }


def test_execute(input, expected_result):
    assert ProcessAdhocPptx().execute(input) == expected_result
