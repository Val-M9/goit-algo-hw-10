import pulp

model = pulp.LpProblem('Profit maximising', pulp.LpMaximize)

lemonade = pulp.LpVariable('lemonade', lowBound=0, cat='Integer')
juice = pulp.LpVariable('juice', lowBound=0, cat='Integer')

# Цільова функція
model += lemonade + juice, 'Profit'

# Обмеження
model += 2 * lemonade + juice <= 100  # Обмеження по ресурсу води
model += lemonade <= 50  # Обмеження по цукру
model += lemonade <= 30  # Обмеження по лимонному соку
model += 2 * juice <= 40  # Обмеження по фруктовому пюре

model.solve()

print(f'Для використання всіх ресурсів необхідно виготовити лемонаду: {
      pulp.value(lemonade)} одиниць та соку: {pulp.value(juice)} одиниць')
