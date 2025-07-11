from src.filter import process_bank_search
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.reader_csv_excel import read_csv, read_excel
from src.utils import open_json
from src.widget import get_date, mask_account_card


def main():
    """Функция, которая отвечает за основную логику проекта и связывает функциональности между собой."""
    print("Привет! Добро пожаловать в программу работы "
          "с банковскими транзакциями.\n"
          "Выберите необходимый пункт меню:\n"
          "1. Получить информацию о транзакциях из JSON-файла\n"
          "2. Получить информацию о транзакциях из CSV-файла\n"
          "3. Получить информацию о транзакциях из XLSX-файла\n")
    while True:
        user_input = input("Введите номер пункта меню ")
        if user_input == "1":
            print("Для обработки выбран JSON-файл")
            transaction_data = open_json("data/operation.json")
            break
        elif user_input == "2":
            print("Для обработки выбран CSV-файл")
            transaction_data = read_csv("data/transactions.csv")
            break
        elif user_input == "3":
            print("Для обработки выбран XLSX-файл")
            transaction_data = read_excel("data/transactions_excel.xlsx")
            break
        else:
            print("Неверный ввод. Пожалуйста выберите один из предложенных пунктов меню.")
    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию.\n"
              "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        user_state = input("Введите статус ").upper()
        if user_state == "EXECUTED" or user_state == "CANCELED" or user_state == "PENDING":
            print(f"Операции отфильтрованы по статусу {user_state}")
            transaction_data = filter_by_state(transaction_data, state=user_state)
            break
        else:
            print(f"Статус операции {user_state} недоступен.")
    print("Отсортировать операции по дате? ДА/НЕТ")
    user_sort = input("Введите ").upper()
    if user_sort == "ДА":
        print("Отсортировать ПО ВОЗРАСТАНИЮ/ ПО УБЫВАНИЮ")
        user_sort_p = input("Введите ").upper()
        if user_sort_p == "ПО ВОЗРАСТАНИЮ":
            transaction_data = sort_by_date(transaction_data)
        elif user_sort_p == "ПО УБЫВАНИЮ":
            transaction_data = sort_by_date(transaction_data)
    print("Выводить только рублевые транзакции? ДА/НЕТ")
    user_rub = input("Введите ").upper()
    if user_rub == "ДА":
        transaction_data = list(filter_by_currency(transaction_data, "RUB"))
    print("Отфильитровать список транзакций по определенному слову? ДА/НЕТ")
    user_filter = input("Введите ").upper()
    if user_filter == "ДА":
        user_filter_w = input("Введите слово ")
        transaction_data = process_bank_search(transaction_data, user_filter_w)
        print(transaction_data)
    print("Распечатываю итоговый список транзакций...")
    if len(transaction_data) == 0:
        print("Не найдено ни одной транзакции,\n"
              "подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(transaction_data)}")
        print("")
        for i in transaction_data:
            d = i["date"]
            print(f"{get_date(d)} {i["description"]}")
            if "Перевод" in i['description']:
                a_1 = i["from"]
                a_2 = i["to"]
                print(f"{mask_account_card(a_1)} -> {mask_account_card(a_2)}")
            elif "Открытие" in i['description']:
                a_3 = i["to"]
                print(f"{mask_account_card(a_3)}")
            print(f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}")
            print("")


main()
