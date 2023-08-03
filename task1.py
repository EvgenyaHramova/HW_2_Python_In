# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

balans = 0
max_balans = 5000000
count_operations = 0
max_count = 3
min_action = 50
percent = 0
min_persent_cash = 30
max_persent_cash = 600
rate_cash = 0.015
rate_action = 0.03
rate_wealth = 0.1


while balans >= 0:
    action = input('Выберите необходимое действие:\n1 - пополнить баланс, 2 - снять деньги, 3 - выйти из системы \n')

    if action == '1':
        insert = int(input('Введите сумму для пополнения баланса: '))
        if insert % min_action == 0:
            balans = balans + insert
            count_operations += 1
            print('Ваш баланс: ', balans)
            if count_operations == max_count:
                percent = balans * rate_action
                balans = balans + percent
                count_operations = 0
                print('Ваш баланс: ', round(balans, 2), ', в т.ч. начислены проценты: ', round(percent, 2),'\n')
        else:
            print('Сумма пополнения должна быть кратна 50. Попробуйте еще раз')
        if balans > max_balans:
            percent_wealth = balans * rate_wealth
            balans = balans - percent_wealth
            print(f'Ваш баланс: {round(balans, 2)} с учетом списания процента на богатство в сумме {percent_wealth}')
   
    if action == '2':
        cash = int(input('Введите сумму для снятия денежных средств с баланса: '))
        percent_cash = cash * rate_cash
        if percent_cash < min_persent_cash:
            percent_cash = min_persent_cash

        if percent_cash > max_persent_cash:
            percent_cash = max_persent_cash

        if balans == 0 or balans < (cash + percent_cash):
            print('Недостаточно средств для проведения операции')
        else:
            if cash % min_action == 0:
                
                balans = balans - cash - percent_cash
                count_operations += 1
                print('Ваш баланс: ', round(balans, 2), ', в т.ч. удержаны проценты cо снимаемой суммы: ', round(percent_cash, 2))
                if count_operations == max_count:
                    percent = balans * rate_action
                    balans = balans - percent
                    count_operations = 0
                    print('Ваш баланс: ', round(balans, 2), ', в т.ч. удержаны проценты: ', round(percent, 2))
            else:
                print('Сумма снятия должна быть кратна 50. Попробуйте еще раз')       
    
    if action == '3':
        print('Вы вышли из системы')
        break

