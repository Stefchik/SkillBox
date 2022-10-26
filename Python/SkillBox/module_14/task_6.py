print('Введите координаты монетки:')
x = float(input('X: '))
y = float(input('Y: '))
radius = int(input('Введите радиус: '))
formula = (x * x + y * y) ** 0.5
if formula < radius:
    print('Монетки в области нет.')
else:
    print('Монетка где-то рядом.')