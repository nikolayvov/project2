import json
import logging


logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/utils.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def open_json(path: str) -> list:
    """Функция, которая возвращает список словарей с транзакциями из JSON-файла."""
    with open(path, "r", encoding="utf-8") as f:
        logger.info("Преобразование JSON-файла")
        try:
            return json.load(f)
        except json.JSONDecodeError:
            logger.info("Возврат пустого списка, при отсутствии JSON-объекта")
            return []
        except Exception:
            logger.info("Возврат пустого списка, при наличии любых ошибок")
            return []


# print(open_json("data/operation.json"))
