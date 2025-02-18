import datetime as dt
import time as t


DATE_FORMAT = '%Y-%m-%d %H:%M:%S'


# Подписывайтесь на тгк: фанаты ???


def options():
    print('Опции:')
    print('1. Перевести деньги на другой счет')
    print('2. Снять деньги со счета')
    print('3. Положить деньги на счет')
    print('4. Смотреть историю транзакций')
    print('5. Проверить баланс')
    print('6. Выйти из системы')
    print('----------')


def check_account(items, passes, username, word_to_pass, history):
    print('Проверка...')
    t.sleep(2)
    if username in items.keys(
    ) and username in passes and passes[username] == word_to_pass:
        history.append(f'Вы вошли в аккаунт: {
            dt.datetime.now().strftime(DATE_FORMAT)}')
        return True
    else:
        return False


def send_money(items, sender, getter, amount, history):
    if items[sender] - amount >= 0:
        if getter not in items:
            return f'Аккаунта с именем {getter} не существует!'
        else:
            items[sender] -= amount
            items[getter] += amount
        print('Ожидайте...')
        t.sleep(1.5)
        history.append(f'Вы перевели {getter} {amount}$ {dt.datetime.now(
        ).strftime(DATE_FORMAT)}')
        print('----------')
        return f'Вы перевели {getter} {amount}$'
    else:
        return print('Недостаточно средств')


def get_money(items, needle, amount, history):
    if items[needle] - amount >= 0:
        items[needle] -= amount
        print('Ожидайте...')
        t.sleep(1.5)
        history.append(f'Снято {amount}$ {dt.datetime.now().strftime(
            DATE_FORMAT)}')
        print('----------')
        return f'Снято {amount}$.'
    else:
        return 'Недостаточно средств'


def take_money(items, needle, amount, history):
    items[needle] += amount
    print('Ожидайте...')
    t.sleep(1.5)
    history.append(f'На счет зачислено {amount}$ {dt.datetime.now().strftime(
        DATE_FORMAT)}')
    print('----------')
    return f'На счет зачислено {amount}$'


def check_balance(items, needle, history):
    value_str = f'{items[needle]:.2f}'
    print('Ожидайте...')
    t.sleep(1)
    history.append(f'Вы проверяли баланс {dt.datetime.now().strftime(
        DATE_FORMAT)}')
    print('----------')
    return f'На вашем счету {value_str}$'


def check_history(history):
    for item in history:
        print(item)
