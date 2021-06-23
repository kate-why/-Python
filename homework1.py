#Task_1
a = 15
b = a / 9
c = 'lol'

d = int(input('vvedi 4islo, epta '))
e = str(input('vvedi stroku, heh '))

print('a', a)
print('b', b)
print('c', c)
print('d', d)
print('e', e)

#Task_2
s = int(input('Time in seconds: '))
h = s // 3600
m = (s - h * 3600) // 60
sec = s % 60
print(f'{h:02}:{m:02}:{sec:02}')

#Task_3
n = input('Enter the number: ')
print(int(n) + int(n + n) + int(n + n + n))

#Task_4
numb = int(input('Enter the number: '))
max = 0
while numb > 0:
    last_dig = numb % 10
    if last_dig > max:
        max = last_dig
        if max == 9:
            break
    numb = numb // 10

print('Max digit in the number: ', max)

#Task_5
proc = float(input('Enter your proceeds: '))
cost = float(input('Enter your costs: '))
fit = proc - cost
if fit > 0:
    print ('You got profit!')
    print ('Profitability: ', fit / proc)
    emp = int(input('Enter the number of employees: '))
    print('Profit per one employee: ', fit / emp)
elif fit == 0:
    print('You got zero profit')
else:
    print('You are at loss')

#Task_6
a = int(input('1st day in km: '))
b = int(input ('Your goal: '))
days = 1
print('Result: ')
while a < b:
    print(f'Day {days}: {round(a, 2)}')
    a = a * 1.1
    days += 1
print(f'On day {days} your goal will be no less than {b} km')



