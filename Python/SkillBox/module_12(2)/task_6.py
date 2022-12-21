import random

class House:
    count = 0

    def __init__(self, family, money: int = 100, food: int = 50, cat_food: int = 30, dirt: int = 0):
        self.family = family
        self.money = money
        self.food = food
        self.cat_food = cat_food
        self.dirt = dirt
        self.earned = 0
        self.food_eaten = 0
        self.cat_eaten = 0
        self.fur_coat = 0
        self.count += 1

    def pollution(self):
        self.dirt += 5

    def life(self):
        for i_resident in self.family:
            if self.dirt >= 90 and not isinstance(i_resident, Cat):
                i_resident.change_happiness(-10)

            if isinstance(i_resident, Cat) and self.cat_food >= 20 <= i_resident.satiety:
                i_resident.eat()

            elif isinstance(i_resident, Cat):
                if random.randint(1, 2) == 1:
                    i_resident.shitting()
                else:
                    i_resident.sleeping()

            elif (isinstance(i_resident, Husband) or
                  isinstance(i_resident, Wife)) \
                    and self.food >= 60 and i_resident.satiety <= 30:
                i_resident.eat()
                print(i_resident.name, 'поел' if isinstance(i_resident, Husband) else 'поела')

            elif isinstance(i_resident, Husband):
                if self.money <= 150:
                    husband.work('экстренную')
                elif husband.happiness <= 50:
                    husband.game()
                elif husband.happiness <= 70:
                    husband.caress_cat()
                else:
                    husband.work('обычную')

            elif isinstance(i_resident, Wife):
                if self.food <= 60 and self.money >= 100:
                    wife.buy_food()
                elif self.cat_food <= 20 and self.money >= 50:
                    wife.buy_cat_food()
                elif self.dirt >= 50:
                    wife.cleaning()
                elif wife.happiness <= 70:
                    wife.caress_cat()
                elif self.money >= 450:
                    wife.buy_fur_coat()
                else:
                    wife.caress_cat()

            elif isinstance(i_resident, Baby):
                if i_resident.satiety <= 30:
                    baby.eat()
                elif i_resident.happiness <= 30:
                    baby.sleeping()
                else:
                    if random.randint(1, 2) == 1:
                        baby.shitting()
                    else:
                        baby.game()

class Residents:
    def __init__(self, name: str, satiety: int, happiness: int = 0):
        self.name = name
        self.satiety = satiety
        self.happiness = happiness

    def eat(self):
        """
        Приём пищи у члена семьи
        """
        self.satiety += 30
        house.food -= 30
        house.food_eaten += 30

    def loss_satiety(self, amount: int = 10):
        """
        Снижение сытости у члена семьи

        :param amount: На сколько снизить сытость
        """
        self.satiety -= amount

    def change_happiness(self, happiness: int):
        """
        Изменение степени счастья у члена семьи

        :param happiness: На сколько изменилась степень счастья
        """
        self.happiness += happiness
        if self.happiness > 100:
            over_happiness = self.happiness - 100
            self.happiness = self.happiness - over_happiness

class Husband(Residents):
    def __init__(self, name: str, satiety: int = 30, happiness: int = 100, salary: int = 150):
        super().__init__(name, satiety, happiness)
        self.salary = salary

    def work(self, work_type: str):
        self.loss_satiety()
        house.money += self.salary
        house.earned += self.salary
        print(f'{self.name} сходил на {work_type} работу')

    def caress_cat(self):
        self.loss_satiety()
        self.change_happiness(5)
        print(f'{self.name} погладил кота')

    def game(self):
        self.loss_satiety()
        self.change_happiness(20)
        print(f'{self.name} поиграл в игру')

class Wife(Residents):
    def __init__(self, name: str, satiety: int = 30, happiness: int = 100):
        super().__init__(name, satiety, happiness)

    def buy_food(self):
        self.loss_satiety()
        house.money -= 100
        house.food += 100
        print(f'{self.name} сходила в магазин за продуктами')

    def buy_cat_food(self):
        self.loss_satiety()
        house.money -= 50
        house.cat_food += 50
        print(f'{self.name} сходила в магазин за едой для кота')

    def caress_cat(self):
        self.loss_satiety()
        self.change_happiness(5)
        print(f'{self.name} погладила кота')

    def buy_fur_coat(self):
        self.loss_satiety()
        self.change_happiness(60)
        house.money -= 350
        house.fur_coat += 1
        print(f'{self.name} купила шубу')

    def cleaning(self):
        if house.dirt > 100:
            house.dirt -= 100
        else:
            house.dirt = 0
        self.satiety -= 10
        print(f'{self.name} навела порядок в доме')

class Cat(Residents):
    def __init__(self, name: str, satiety: int = 30):
        super().__init__(name, satiety)

    def eat(self):
        self.satiety += 20
        house.cat_food -= 10
        house.cat_eaten += 10
        print(f'{self.name} поел(а). Еды осталось: {house.cat_food}')

    def sleeping(self):
        self.loss_satiety()
        print(f'{self.name} поспал(а)')

    def shitting(self):
        self.loss_satiety()
        house.dirt += 5
        print(f'{self.name} подрал(а) обои')

class Baby(Residents):
    def __init__(self, name: str, satiety: int = 30, happiness: int = 100, saturation: int = 10):
        super().__init__(name, satiety, happiness)
        self.saturation = saturation

    def game(self):
        """
        Во время игры ребёнок становится счастливым
        """
        self.loss_satiety()
        self.change_happiness(20)
        print(f'{self.name} поиграл(а) в игру')

    def eat(self):
        """
        Ребёнку нужно меньше еды и он становится сытым в два раза больше
        """
        self.satiety += self.saturation * 2
        house.food -= self.saturation
        house.food_eaten += self.saturation
        print(f'{self.name} поел(а)')

    def sleeping(self):
        """
        Когда ребёнок спит он быстро восстанавливает степень счастья
        """
        self.loss_satiety()
        self.change_happiness(60)
        print(f'{self.name} поспал(а)')

    def shitting(self):
        self.loss_satiety()
        self.change_happiness(-20)
        house.dirt += 10
        print(f'{self.name} не успел(а) добежать до горшка. Степень счастья: {self.happiness}')

def life_dead(family) -> bool:
    for i_elem in family:
        if i_elem.satiety <= 0:
            print('Один из жильцов умер от голода')
            return True
        elif i_elem.happiness == 0 and not isinstance(i_elem, Cat):
            print('Один из жильцов умер от депрессии')
            return True
        else:
            return False

husband = Husband('Александр')
wife = Wife('Наталья')
baby = Baby('Елена')
cat_mather = Cat('Лысая')
cat_baby = Cat('Кассиопея')
family_list = [husband, wife, baby, cat_mather, cat_baby]
house = House(family_list)

for i_day in range(1, 366):
    print(f'День {i_day}')
    house.pollution()
    if life_dead(family_list):
        print('\nЭксперимент провалился')
        break
    elif i_day == 365:
        print('\nЭксперимент удался')
        break
    else:
        house.life()

print(f'\nЗа год:'
      f'\nДомов заселено: {house.count}'
      f'\nКуплено шуб: {house.fur_coat}'
      f'\nЗаработано денег: {house.earned}'
      f'\nСъедено еды: {house.food_eaten}'
      f'\nКот съел еды: {house.cat_eaten}')
