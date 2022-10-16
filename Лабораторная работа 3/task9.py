salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен
months_ = 1  # счетчик месяцев, когда начинается повышение цен
need_money = 0  # количество денег, чтобы прожить 10 месяцев

while months_ <= months:
    need_money += spend - salary
    spend += spend * increase
    months_ += 1

print(round(need_money))
