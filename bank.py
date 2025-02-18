import bank_functions as bf
import datetime as dt
import time as t
from decimal import Decimal


# Подписывайтесь на тгк: фанаты ???


DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
history: list = []

accounts = {
    'alexey': Decimal(0),
    'eugene': Decimal(228.69),
    'peter': Decimal(52.52)
}

passwords = {
    'alexey': 'admin',
    'eugene': 'pass',
    'peter': 'meme'
}

print('--- Супер Банк ---')
print('Сегодня:', dt.datetime.now().strftime(DATE_FORMAT))

while True:
    name = input('Введите имя: ')
    password = input('Введите пароль: ')
    if bf.check_account(accounts, passwords, name, password, history):
        print('Успешно!')
        break
    else:
        print('Неверный логин или пароль')

while True:
    t.sleep(0.3)
    print('----------')
    t.sleep(0.3)
    bf.options()
    value = str(input('Выберите опцию: '))
    print('----------')
    if int(value) == 1:
        recipient = str(input('Укажите получателя: '))
        value_to_send = Decimal(input('Укажите сумму для перевода: '))
        print(bf.send_money(accounts, name, recipient, value_to_send, history))
    elif int(value) == 2:
        money_to_get = Decimal(input('Укажите сумму для снятия: '))
        print(bf.get_money(accounts, name, money_to_get, history))
    elif int(value) == 3:
        money_to_take = Decimal(input('Укажите сумму для внесения: '))
        print(bf.take_money(accounts, name, money_to_take, history))
    elif int(value) == 4:
        bf.check_history(history)
    elif int(value) == 5:
        print(bf.check_balance(accounts, name, history))
    elif int(value) == 6:
        if str(input('Вы уверены? (Y/N) ')).lower() == 'y':
            t.sleep(2)
            print('До свидания!')
            exit()
    elif value != 1 or 2 or 3 or 4 or 5 or 6:
        print('Опции не существует')
    else:
        continue
