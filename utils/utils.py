import json
from datetime import datetime

import requests as requests
from utils.transaction import Transaction
from utils.constants import JSON_DATA_PATH
import re


def get_transactions(input_json):
    """Получает данные с внешнего ресурса, передает их в класс transaction.
     """
    json_path = input_json  #JSON_DATA_PATH
    user_transactions = []
    raw_data = requests.get(json_path)
    data = json.loads(raw_data.text)

    for raw_transaction in data:
        if bool(raw_transaction):
            transaction = Transaction(
                raw_transaction.get("id", " "),
                raw_transaction.get("state", " "),
                raw_transaction.get("date", " "),
                raw_transaction.get("operationAmount", " ").get("amount", " "),
                raw_transaction.get("operationAmount", " ").get("currency", " ").get("name", " "),
                raw_transaction.get("operationAmount", " ").get("currency", " ").get("code", " "),
                raw_transaction.get("description", " "),
                raw_transaction.get("from", " "),
                raw_transaction.get("to", " ")
            )
        else:
            transaction = Transaction(
                "not found",
                "not found",
                "not found",
                "not found",
                "not found",
                "not found",
                "not found",
                "not found",
                "not found",
            )
        user_transactions.append(transaction)

    return user_transactions


def get_executed_only(input_json):
    """Выбирает только выполненные клиентом операции.
    """
    executed_only = []
    for entry in get_transactions(input_json):
        if entry.state == "EXECUTED":
            executed_only.append(entry)

    return executed_only


def sorted_by_datetime(input_json):
    """Сортирует выполненные клиентом операции по дате и времени и возвращает последние 5 операций.
    """
    list_to_sort = get_executed_only(input_json)
    temp_dictionary = {}
    for entry in list_to_sort:
        temp_dictionary[entry] = entry.date

    sorted_tuple = sorted(temp_dictionary.items(), key=lambda x: x[1])

    return list(dict(sorted_tuple).keys())[-5:]


def account_hide(account):
    """Возвращает замаскированный номер счета на который был выполнен перевод.
    """
    account_number = account[5:]

    return '*' * len(account_number[14:-4]) + account_number[-4:]


def card_hide(card):
    """Возвращает замаскированный номер карты с которого был выполнен перевод.
    """
    name_card = card[:len(card) - 16]
    card_number = card[-16:]
    private_number = card_number[:6] + (len(card_number[6:-4]) * '*') + card_number[-4:]
    private_number = re.sub(r'.{4}', r'\g<0> ', private_number[::-1])[::-1]

    return name_card + private_number


def output(transaction):
    """Выводит необходимую информацию в требуемом формате.
    """
    print(f'{datetime.strptime(transaction.date, "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")} Перевод организации\n'
          f'{card_hide(transaction.from_field)} -> Счет {account_hide(transaction.to)}\n'
          f'{transaction.operationAmount_amount} {transaction.operationAmount_currency_name}\n '
          f'')
