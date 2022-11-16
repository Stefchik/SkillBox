count_cells = int(input('Количество клеток: '))
inappropriate_values = []
for i in range(1, count_cells + 1):
    efficiency = int(input(f'Эффективность {i} клетки: '))
    if efficiency < i:
        inappropriate_values.append(efficiency)
print('Неподходящие значения:', inappropriate_values)