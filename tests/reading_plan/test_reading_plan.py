from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501
from unittest.mock import Mock, patch
import pytest


mock_db = [
    {
        "url": "https://www.tecmundo.com.br/voxel",
        "title": "Voxel",
        "timestamp": "2021-03-18T14:00:00",
        "writer": "João Gabriel",
        "summary": "Resumo",
        "category": "games",
        "reading_time": 5,
    },
    {
        "url": "https://www.tecmundo.com.br/voxel",
        "title": "Voxel",
        "timestamp": "2021-03-18T14:00:00",
        "writer": "João Gabriel",
        "summary": "Resumo",
        "category": "games",
        "reading_time": 10,
    },
    {
        "url": "https://www.tecmundo.com.br/voxel",
        "title": "Voxel",
        "timestamp": "2021-03-18T14:00:00",
        "writer": "João Gabriel",
        "summary": "Resumo",
        "category": "games",
        "reading_time": 15,
    },
]

mock_find_news = Mock(return_value=mock_db)


@patch(
    "tech_news.analyzer.reading_plan.find_news",
    mock_find_news,
)
def test_reading_plan_group_news():
    result = ReadingPlanService.group_news_for_available_time(10)

    assert result == {
        "readable": [
            {"chosen_news": [("Voxel", 5)], "unfilled_time": 5},
            {"chosen_news": [("Voxel", 10)], "unfilled_time": 0},
        ],
        "unreadable": [("Voxel", 15)],
    }

    with pytest.raises(ValueError):
        ReadingPlanService.group_news_for_available_time(0)
