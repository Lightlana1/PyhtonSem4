# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции - функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег


PERCENT_PULL = 0.015
# Кол-во последовательных операция для начисления %
OPERATION_ADDED = 2
# Процент пополнения карты
PERCENT_ADD = 0.03
# Минимум удержания
MIN_PERCENTAGE = 30
# Максимум удержания
MAX_PERCENTAGE = 600
# Минимальная купюра
MIN_BANKNOTE = 50
# Налогооблагаемая сумма
MIN_TAX = 5_000_000
# Ставка налогообложения
PERCENT_TAX = 0.1

# лог операций
logging = []


def save_log(operation: str):
    logging.append(operation)


def task_choice() -> None:
    try:
        choice = int(input("Выберите задачу: 1. Пополнить 2. Снять 3. Выйти \n"))
        return choice

    except ValueError:
        print("Неверный ввод!")


# удержание налога
def tax_pay(summ: float) -> float:
    tax = summ * PERCENT_TAX

    summ -= tax
    return tax


# удержание процента за снятие
def task_procent(summ: float) -> float:
    tax = summ * PERCENT_PULL
    if tax < MIN_PERCENTAGE:
        tax = MIN_PERCENTAGE
    if tax > MAX_PERCENTAGE:
        tax = MAX_PERCENTAGE
    print(f"Налог: {tax:.2f}")
    return tax


# Пополнение
def replenish(balance: float) -> (float):
    summ = float(input("Введите сумму: "))

    if summ % 50 == 0:
        balance += summ
        print(f"Баланс пополнен на сумму: {summ:.2f}")
        if balance > MIN_TAX:
            balance -= tax_pay(summ)
            print(f"Списан налог, ваш баланс: {tax_pay(summ):.2f}")

    else:
        print("Недоступная сумма!")

    return balance

# снятие
def take_off(balance: float) -> (bool, float):
    if balance > MIN_TAX:
        balance = tax_pay(balance)

    summ = float(input("Сколько вы желаете снять: "))
    nalog = task_procent(summ)
    if summ % 50 == 0 and balance > summ:
        summ = summ + nalog
        balance -= summ
        print(f"Снято средств с учетом налога: {summ:.2f}")
        if balance > MIN_TAX:
            balance -= tax_pay(summ)
            print(f"Списан налог, ваш баланс: {tax_pay(summ):.2f}")

    else:
        print("Недоступная сумма!")

    return balance

#Начисление процентов после каждой 3-й операции
def third_count(count: int, balance: float) -> float:
    if count == OPERATION_ADDED:
        profit = balance*PERCENT_ADD
        balance += profit
        print(f"Вам начислено процентов: {profit:.2f}")
    return balance

#Подсчёт операций
def counting(count: int) -> int:
    if count > OPERATION_ADDED:
        count -= OPERATION_ADDED
    else:
        count +=1
    return count

def main() -> object | str:
    # начальный баланс
    balance: float = 0
    # счетчик операци
    operation_count: int = 0

    menu = task_choice()
    while menu < 3:
        if menu == 1:
            balance = replenish(balance)
            save_log(f'Пополнение карты. Баланс {balance}')
            balance = third_count(operation_count, balance)
            operation_count = counting(operation_count)

            print(f"Ваш баланс: {balance}")
            print(f'\n')
            menu = task_choice()

        if menu == 2:
            balance = take_off(balance)
            save_log(f'Снятие средств. Баланс {balance}')
            balance = third_count(operation_count, balance)
            operation_count = counting(operation_count)
            print(f"Ваш баланс: {balance}")
            print(f'\n')
            menu = task_choice()


if __name__ == "__main__":
    main()
