from __future__ import annotations
from dataclasses import dataclass
from random import randint

@dataclass
class House:
    food: int = 50
    money: int = 0

    def store(self, amount=1):
        self.money += amount

    def buy(self, amount=1, cost=1):
        # Но тогда мы не купим в кредит
        money = max(0, amount * cost)
        self.money -= money
        self.food += amount

    def consume(self, amount=1) -> int:
        food = max(0, self.food - amount)
        result = self.food - food
        self.food = food
        return result

@dataclass
class Person:
    name: str
    house: House
    satiety: int = 50

    def eat(self):
        self.satiety += self.house.consume()

    def work(self, amount=1):
        self.satiety -= amount
        self.house.store()

    def play(self, amount=1):
        self.satiety -= amount

    def shop(self, amount=1):
        self.house.buy(amount)

    @property
    def is_alive(self) -> bool:
        return self.satiety >= 0

    def tick(self):
        if not self.is_alive:
            raise ValueError(f"{self.name} умер!")
        dice = randint(1, 6)
        if self.satiety < 20:
            self.eat()
        elif self.house.food < 10:
            self.shop()
        elif self.house.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.play()

house = House()
person = Person("Артём", house)
for _ in range(365):
    person.tick()
else:
    print(f"{person.name} выжил!")

house2 = House()
people = Person("Артём", house2), Person("Лиза", house2)
for _ in range(365):
    for person in people:
        person.tick()
else:
    names = (person.name for person in people)
    print(*names, sep=", ", end=" ")
    print("выжили!")
