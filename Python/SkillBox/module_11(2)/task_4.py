class Parent:
    childrens = []

    def __init__(self, name: str, age: int, childrens):
        self.name = name
        self.age = age
        for child in childrens:
            if age - child.age > 16:
                self.childrens.append(child)

    def __str__(self):
        return self.name + ' ' + str(self.age) + '\n' + '\n'.join(str(child) for child in self.childrens)

    def set_calm(self, children):
        for child in self.childrens:
            if child is children:
                child.calm = True

    def set_hunger(self, children):
        for child in self.childrens:
            if child is children:
                child.hunger = True

class Children:

    def __init__(self, name: str, age: int, calm: bool, hunger: bool):
        self.name = name
        self.age = age
        self.calm = calm
        self.hunger = hunger

    def __str__(self):
        state_calm = ('Спокоен' if self.calm else 'Раздражен')
        state_hunger = ('Сыт' if self.hunger else 'Голоден')
        return ('{} {} лет {} {}'.format(
            self.name, self.age, state_calm, state_hunger))

lena = Children('Лена', 1, True, True)
vika = Children('Вика', 13, True, False)
misha = Children('Миша', 26, False, True)
natasha = Parent('Наташа', 45, [lena, vika, misha])
print(natasha)
natasha.set_calm(misha)
print(natasha)
natasha.set_hunger(vika)
print(natasha)
