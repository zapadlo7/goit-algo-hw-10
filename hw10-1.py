import pulp

# Створюємо змінні для кількості продуктів "Лимонад" та "Фруктовий сік"
x1 = pulp.LpVariable("Лимонад", lowBound=0, cat='Integer')
x2 = pulp.LpVariable("Фруктовий сік", lowBound=0, cat='Integer')

# Ініціалізуємо модель
model = pulp.LpProblem("Maximize Production", pulp.LpMaximize)

# Додаємо обмеження на використання ресурсів
model += 2 * x1 + x2 <= 100, "Вода"
model += x1 <= 50, "Цукор"
model += x1 <= 30, "Лимонний сік"
model += 2 * x2 <= 40, "Фруктове пюре"

# Додаємо функцію максимізації (максимізуємо виробництво "Лимонаду" та "Фруктового соку")
model += x1 + x2

# Розв'язуємо модель
model.solve()

# Виводимо результати
print("Результати:")
for variable in model.variables():
    print(f"{variable.name}: {variable.varValue} одиниць")

print("Максимальна кількість продуктів: ", pulp.value(model.objective))
