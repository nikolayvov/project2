from unittest.mock import patch
from src.reader_csv_excel import read_csv, read_excel


@patch("pandas.read_csv")
def test_read_csv(mock_read_csv):
    operations = [{'id': 4699552.0, 'state': 'EXECUTED', 'date': '2022-03-23T08:29:37Z',
                   'amount': 23423.0, 'currency_name': 'Peso', 'currency_code': 'PHP',
                   'from': 'Discover 7269000803370165', 'to': 'American Express 1963030970727681',
                   'description': 'Перевод с карты на карту'}]
    mock_read_csv.return_value.to_dict.return_value = operations
    result = read_csv("f.csv")
    assert result == operations


@patch("pandas.read_excel")
def test_read_excel(mock_read_excel):
    operations = [{'id': 134341.0, 'state': 'CANCELED', 'date': '2022-03-03T08:41:08Z',
                   'ency_code': 'CNY', 'from': 'Счет 38577962752140632721',
                   'to': 'Счет 47657753885349826314', 'description': 'Перевод со счета на счет'}]
    mock_read_excel.return_value.to_dict.return_value = operations
    result = read_excel("f.xlsx")
    assert result == operations
