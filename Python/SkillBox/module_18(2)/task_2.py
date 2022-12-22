import re

number_list = ['А578ВЕ777', 'ОР233787', 'К901МН666', 'СТ46599', 'СНИ2929П777', '666АМР666']
private_number = []
taxi_number = []
fail_number = []

def determine_type(number: str) -> None:
    global private_number, taxi_number, fail_number
    if re.fullmatch(r'[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}', number):
        private_number.append(number)
    elif re.fullmatch(r'[АВЕКМНОРСТУХ]{2}\d{5,6}', number):
        taxi_number.append(number)
    else:
        fail_number.append(number)

if __name__ == '__main__':
    for item in number_list:
        determine_type(item)

    if len(private_number) > 0:
        print('Список номеров частных автомобилей:', private_number)
    if len(taxi_number) > 0:
        print('Список номеров такси:', taxi_number)
    if len(fail_number) > 0:
        print('Список не верных номеров:', fail_number)
