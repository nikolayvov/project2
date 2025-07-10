import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Функция, которая возвращает список словарей с транзакциями по данной строке в описании."""
    result = []
    re_pattern = re.compile(search, re.IGNORECASE)
    for operation in data:
        if re_pattern.search(str(operation.get("description", ""))):
            result.append(operation)
    return result


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Функция, которая возвращает словарь ключ-название категории значение-количество операций."""
    count_categories = []
    for operation in data:
        if operation.get("description", "") in categories:
            count_categories.append(operation.get("description", ""))
    return dict(Counter(count_categories))
