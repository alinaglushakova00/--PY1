money_capital = 10000
salary = 5000
spend = 6000
increase = 1.05

month = 0  # количество месяцев, которое можно прожить

while money_capital >= spend :

    money_capital -= spend
    money_capital += salary
    spend *= increase
    month += 1

print(month)
