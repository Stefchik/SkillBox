file = open('zen.txt', 'r')
s = file.readlines()
s.reverse()
print(''.join(s))
