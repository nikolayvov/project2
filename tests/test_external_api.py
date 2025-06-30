from unittest.mock import patch
from src.external_api import convert_rub


@patch("requests.get")
def test_convert_rub(mock_get):
    mock_get.return_value.json.return_value = {"result": 649000}
    result = convert_rub({
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        })
    assert result == 649000
