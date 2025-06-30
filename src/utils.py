import json


def open_json(path: str) -> list:
    """Функция, которая возвращает список словарей с транзакциями из JSON-файла."""
    with open(path, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []
        except Exception:
            return []


# print(open_json("../data/operation.json"))
