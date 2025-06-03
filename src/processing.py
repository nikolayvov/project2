from typing import List, Dict, Any


def filter_by_state(transaction_list: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Функция, которая фильтрует список словарей по значению ключа 'state'
    :param transaction_list: список словарей (транзакций)
    :param state: статус операции для фильтрации
    :return: отфильтрованный по статусу список транзакций
    """
    return [transaction for transaction in transaction_list if transaction.get("state") == state]


def sort_by_date(transaction_list: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Функция, которая сортирует список словарей по дате
    :param transaction_list: список словарей (транзакций)
    :return: отсортированный по дате список транзакций
    """
    return sorted(transaction_list, key=lambda item: item["date"], reverse=True)


print(
    filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)
print(
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)
