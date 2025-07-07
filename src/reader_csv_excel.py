import pandas as pd


def read_csv(file_path: str) -> list[dict]:
    """Функция, которая возвращает список словарей с транзакциями из csv-файла."""
    df = pd.read_csv(file_path, delimiter=";")
    return df.to_dict(orient="records")


def read_excel(file_path: str) -> list[dict]:
    """Функция, которая возвращает список словарей с транзакциями из excel-файла."""
    df = pd.read_excel(file_path)
    return df.to_dict(orient="records")


# if __name__ == "__main__":
    # print(read_csv("data/transactions.csv"))
    # print(read_excel("data/transactions_excel.xlsx"))
