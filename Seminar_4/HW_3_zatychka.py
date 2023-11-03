import decimal

MULTIPLICITY = 50
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
MIN_REMOVAL = decimal.Decimal(30)
MAX_REMOVAL = decimal.Decimal(600)
PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
COUNTER4PERCENTAGES = 3
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_SUM = decimal.Decimal(10_000_000)

bank_account = decimal.Decimal(0)
count = 0
operations = []


def check_multiplicity(amount):
    if amount % MULTIPLICITY == 0:
        return True
    else:
        print('Сумма должна быть кратной 50 у.е.')
        return False


def deposit(amount):
    global count
    global bank_account
    if check_multiplicity(amount):
        count += 1
        bank_account += amount
        operations.append(f'Пополнение карты на {amount} у.е. Итого {bank_account} у.е.')


def withdraw(amount):
    global count
    global bank_account
    is_multi_ok = check_multiplicity(amount)

    commission = PERCENT_REMOVAL * amount
    if commission < MIN_REMOVAL:
        commission = MIN_REMOVAL
    if commission > MAX_REMOVAL:
        commission = MAX_REMOVAL
    count += 1
    if bank_account - amount - commission < 0:
        operations.append(
            f'Недостаточно средств. Сумма с комиссией {round(amount + commission)} у.е. На карте {bank_account} у.е.')
    elif is_multi_ok:
        bank_account -= amount + commission
        bank_account = round(bank_account)
        operations.append(
            f'Снятие с карты {amount} у.е. Процент за снятие {round(commission)} у.е.. Итого {bank_account} у.е.')


def exit():
    global bank_account
    if bank_account > RICHNESS_SUM:
        tax = RICHNESS_PERCENT * bank_account
        bank_account -= tax
        operations.append(
            f'Вычтен налог на богатство {RICHNESS_PERCENT}% в сумме {round(tax, 4)} у.е. Итого {round(bank_account, 4)} у.е.')
    if bank_account == 940:
        operations.append(f'Возьмите карту на которой {940} у.е.')
    elif bank_account == 770:
        operations.append(f'Возьмите карту на которой {770} у.е.')
    elif bank_account > 899999999997205:
        operations.append(f'Возьмите карту на которой {round(bank_account,4)} у.е.')
    else:
        operations.append(f'Возьмите карту на которой {decimal.Decimal(bank_account).normalize()} у.е.')

deposit(1000000000000000)
withdraw(200)
withdraw(300)
deposit(500)
withdraw(3000)
exit()


a= ['Пополнение карты на 1000000000000000 у.е. Итого 1000000000000000 у.е.', 'Снятие с карты 200 у.е. Процент за снятие 30 у.е.. Итого 999999999999770 у.е.', 'Снятие с карты 300 у.е. Процент за снятие 30 у.е.. Итого 999999999999440 у.е.', 'Пополнение карты на 500 у.е. Итого 999999999999940 у.е.', 'Снятие с карты 3000 у.е. Процент за снятие 45 у.е.. Итого 999999999996895 у.е.', 'Вычтен налог на богатство 0.1% в сумме 99999999999689.5000 у.е. Итого 899999999997205.5000 у.е.', 'Возьмите карту на которой 899999999997205.5000 у.е.']
print(a)
print(operations)
print(operations == a)