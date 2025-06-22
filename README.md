## Описание:

Проект "Домашка" - создание виджета банковских операций клиента

## Установка:

1. Клонируйте репозиторий:
```
git clone git@github.com:nikolayvov/project2.git
```

2. Установите зависимости:
```
poetry install
```

## Тестирование:

Юнит-тесты были реализованы с помощью pytest. Покрытие составляет 100%.

Запустить тесты:

```
pytest .
```

Покрытие:

```
pytest --cov=src .
```
### Модуль "Генераторы"

```
src/generators.py:card_number_generator - генератор номеров карт
src/generators.py:transaction_descriptions - выдача описания операций
src/generators.py:filter_by_currency - выдача трансакций по коду вылюты
```

### Модуль "Декораторы"

```
src/decorators.py:log - логирует результат выполнения функции и ошибки

```