class Student:

    def __init__(self, full_name: str, group_number: str, progress: tuple):
        self.full_name = full_name
        self.group_number = group_number
        self.progress = progress

    def give_average(self) -> float:
        return round(sum(self.progress) / len(self.progress), 2)

    def __str__(self):
        return f'ФИ: {self.full_name} - № группы: {self.group_number} - Средний балл: {self.give_average()}'

def receiving_data():
    name = input('Фамилия Имя: ')
    group = input('Номер группы: ')
    ball = tuple(map(int, input('Оценки (через пробел): ').split()))
    return name, group, ball

list_student = [Student(*receiving_data()) for _ in range(10)]
print('Список студентов:')
for student in list_student:
    print(student)
print()

list_student.sort(key=lambda x: x.give_average())
print('Список студентов отсортированный:')
for student in list_student:
    print(student)
