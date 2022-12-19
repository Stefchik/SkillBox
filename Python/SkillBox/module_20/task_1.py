students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology', 'swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def interest_len(data):
    interests = []
    last_names = ''
    for i in data:
        interests += (data[i]['interests'])
        last_names += data[i]['surname']
    interests.sort()
    return interests, len(last_names)


pairs = [(i, students[i]['age']) for i in students]
print('Список пар "ID студента - Возраст":', pairs)

inter_len = interest_len(students)
print('Полный список интересов всех студентов:', inter_len[0])
print('Общая длина всех фамилий студентов:', inter_len[1])
