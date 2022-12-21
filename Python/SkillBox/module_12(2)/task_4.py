from random import randint, choice
from typing import Union

names = ['Алексей', 'Евгений', 'Иван', 'Петр', 'Семен', 'Антон', 'Максим']
surnames = ['Александрович', 'Николаевич', 'Владимирович', 'Евгеньевич', 'Антонович']

def generate_person():
    name = choice(names)
    surname = choice(surnames)
    return name, surname

class Person:
    def __init__(self, name: str, surname: str, job_title: str = ''):
        self.__name = name
        self.__surname = surname
        self.job_title = job_title

    def __str__(self):
        return f'{self.__name} {self.__surname}.'

class Employee(Person):
    def calc_salary(self) -> (Union[int, float]):
        raise Exception('This method must be overriden')

    def __str__(self):
        return super().__str__() + f' Должность: {self.job_title}, Зарплата: {self.calc_salary()}'

class Manager(Employee):
    def calc_salary(self) -> (Union[int, float]):
        return 13000

class Agent(Employee):
    sales: (Union[int, float])

    def calc_salary(self) -> (Union[int, float]):
        return 5000 + .05 * self.sales

class Worker(Employee):
    hours: (Union[int, float])

    def calc_salary(self) -> (Union[int, float]):
        return 100 * self.hours

if __name__ == '__main__':
    employees = list()

    for _ in range(3):
        employees.append(Manager(*generate_person(), 'Manager'))

    for _ in range(3):
        agent = Agent(*generate_person(), 'Agent')
        agent.sales = randint(2000, 10000)
        employees.append(agent)

    for _ in range(3):
        worker = Worker(*generate_person(), 'Worker')
        worker.hours = randint(20, 50)
        employees.append(worker)

    for emp in employees:
        print(emp)