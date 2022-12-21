class Cell:
    states = {0: ' ', 1: 'X', 2: 'O'}

    def __init__(self, index: int):
        self.index = index
        self.state = 0

    def __str__(self):
        if self.state == 0:
            result = f'{self.index}'
        else:
            result = f'{Cell.states[self.state]}'
        return result

    def set_status(self, state: states):
        """ Да, да, да. Тут лишняя проверка. Функция is_free была добавлена позже. """
        if self.state == 0:
            self.state = state
        self.print_state()

    def is_free(self) -> bool:
        if self.state == 0:
            return True
        print('Данная ячейка занята.')
        return False

    def print_state(self):
        print(f'Ячейка {self.index} сейчас {Cell.states[self.state]}.')


class Player:
    def __init__(self, name: str):
        self.name = name
        self.figure: Cell.states = 0
        self.my_turn = False

    def set_symbol(self, symbol: str):
        if symbol == 'X':
            self.figure = 1
        else:
            self.figure = 2

class Board:
    def __init__(self):
        self.cells = [Cell(index) for index in range(1, 10)]
        self.battle = True

    def check_win(self):
        win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for cell in win_coord:
            sum_row = self.cells[cell[0]].state + self.cells[cell[1]].state + self.cells[cell[2]].state
            if sum_row > 0:
                if self.cells[cell[0]].state == self.cells[cell[1]].state == self.cells[cell[2]].state:
                    self.battle = False
                    return True
        return False

    def draw_board(self):
        print("-" * 13)
        for i in range(3):
            print("|", self.cells[0 + i * 3], "|", self.cells[1 + i * 3], "|", self.cells[2 + i * 3], "|")
            print("-" * 13)

    def count_free_cell(self):
        """ Есть ли у нас свободные ячейки """
        count = 0
        for cell in self.cells:
            if cell.state == 0:
                count += 1
        return count

    def turn(self, player: Player, cell: int):
        self.cells[cell].set_status(player.figure)
        if self.check_win():
            print(f'{player.name}, ходивший фигурой "{Cell.states[player.figure]}" победил.')
            self.draw_board()
        if self.count_free_cell() == 0:
            self.draw_board()
            self.battle = False
            print('\nБольше нет свободных ячеек.\nВ этот раз ничья.')

p1 = Player(input('Введите имя первого игрока: '))
p2 = Player(input('Введите имя второго игрока: '))

while True:
    answer = input(f'\nЧем будет ходить {p1.name}:\n1 - X\n2 - O\nВыбор: ')
    if answer == '1':
        p1.figure = 1
        p2.figure = 2
        break
    elif answer == '2':
        p1.figure = 2
        p2.figure = 1
        break

while True:
    answer = input(f'\nКто будет ходить первым:\n1 - {p1.name}\n2 - {p2.name}\nВыбор: ')
    if answer == '1':
        p1.my_turn = True
        break
    elif answer == '2':
        p2.my_turn = True
        break

brd = Board()

while True:
    brd.draw_board()
    if p1.my_turn:
        my_cell = int(input(f'{p1.name} ходит в ячейку: '))
        if brd.cells[my_cell - 1].is_free():
            brd.turn(p1, my_cell - 1)
            p1.my_turn = False
            p2.my_turn = True
    elif p2.my_turn:
        my_cell = int(input(f'{p2.name} ходит в ячейку: '))
        if brd.cells[my_cell - 1].is_free():
            brd.turn(p2, my_cell - 1)
            p1.my_turn = True
            p2.my_turn = False
    else:
        print('Я тогда поиграю за вас.')
    if not brd.battle:
        break
