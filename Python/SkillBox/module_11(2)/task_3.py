class Circle:
    pi = 3.14159

    def __init__(self, x=0, y=0, r=1):
        self.x = x
        self.y = y
        self.r = r

    def get_area(self) -> float:
        return self.r * self.r * self.pi

    def get_perimeter(self) -> float:
        return 2 * self.r * self.pi

    def scale(self, k: float):
        self.r *= k

    def is_intersect(self, other) -> bool:
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2 <= (self.r + other.r) ** 2

print('Окружность 1')
c1 = Circle(2, 2, 2)
print(c1.get_area())
print(c1.get_perimeter())
c1.scale(2)
print(c1.get_area())
print(c1.get_perimeter())

print('\nОкружность 2')
c2 = Circle(3, 3, 3)
print(c2.get_area())
print(c2.get_perimeter())
c2.scale(2)
print(c2.get_area())
print(c2.get_perimeter())

print('\nПересечение')
print(c1.is_intersect(c2))
