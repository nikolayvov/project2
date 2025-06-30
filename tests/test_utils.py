import json
from unittest.mock import patch, mock_open
from src.utils import open_json


mock_data = '''[{
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        }]'''
expected = json.loads(mock_data)


@patch("builtins.open", new_callable=mock_open, read_data=mock_data)
def test_open_json(mock_file):
    result = open_json("f_path.json")
    assert result == expected
