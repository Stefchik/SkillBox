class Gamer:
    def __init__(self, fname, lname, points):
        self.first_name = fname
        self.last_name = lname
        self.points = int(points)

    def __str__(self):
        return f'{self.last_name[0]}. {self.first_name} {self.points}'

    def __repr__(self):
        return f'Игрок: {self.first_name} {self.last_name} - {self.points}'


def sort_by_pionts(points):
    return points.points


first_file = open("first_tour.txt", "r", encoding="utf8")
new_list = []
current_row = 0
limit_points = 0

for row in first_file:
    if current_row > 0:
        data = row.split()
        gamer = Gamer(data[0], data[1], data[2])
        new_list.append(gamer)
    else:
        limit_points = int(row)
    current_row += 1
first_file.close()

new_list.sort(key=sort_by_pionts, reverse=True)


out_list = []

for i in new_list:
    if i.points > limit_points:
        out_list.append(i)

with open("second_tour.txt", "w", encoding='utf-8') as f_out:
    f_out.write(str(len(out_list)) + '\n')
    row = 1
    for i in out_list:
        s = f'{row}) {i}\n'
        f_out.write(s)
        row += 1
    f_out.close()

for i in out_list:
    print(f'{i}')
