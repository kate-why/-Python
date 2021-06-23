#Task_1
from sys import argv

def salary():
    try:
        # hours = float(argv[1])
        # rate = float(argv[2])
        # premium = float(argv[3])
        path, hours, rate, bonus = argv
        hours, rate, bonus = map(float, argv[1:])
        print('Wage: ', hours * rate + bonus)
    except ValueError:
        print('Start the script with three parameters: hours, rate/hour and bonus ')

salary()

#Task_2
list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new = [list[i]for i in range(1, len(list)) if list[i] >  list [i - 1]]
print(new)

#Task_3
lu2 = [i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0]
print(lu2)

#Task_4
list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new = [i for i in list if list.count(i) == 1]
print(new)

#Task_5
from functools import reduce

abc = [i for i in range(100, 1001, 2)]
print(abc)

def multiplication(arg1, arg2):
    return arg1 * arg2

print(reduce(multiplication, abc))

#Task_6.1
from itertools import cycle, count

start = int(input('Enter first number: '))
end = int(input('Enter last number: '))
for i in count(start):
    print(i)
    if i == end:
        break

#Task_6.2
li = input('Enter the list (use a space): ').split()

for el in cycle(li):
    stop = input('Continue iteration? For exit type "no" ')
    if stop.title() == 'No':
        break
    print(el)

#7
def fact(b):
    res = 1
    if b == 0:
        yield f'{b}! = 1'
    for i in range(1, b + 1):
        res *= i
        yield f'{i}! = {res}'

n = int(input('Enter the number (max factorial): '))
for el in fact(n):
    print(el)