#Task_1
list = [90, 870.5, 'hello', [11, 1], (999, 'hi'), {'GO': 1234}]
for el in list:
    print(f'{el} is type: {type(el)}')

#Task_2
list = input('Enter list elements (use a space): ').split()
for i in range (1, len(list), 2): # i = 1 2 3 5 6 7
    list[i - 1], list[i] = list[i], list[i - 1]

print(list)

#Task_3
m = int(input('Enter month: '))
season_dict = {'Winter' : [12, 1, 2], 'Spring' : [3, 4, 5], 'Summer' : [6, 7, 8], 'Autumn' : [9, 10, 11]}
season_list = ['Winter', 'Spring', 'Summer', 'Autumn']

for el in season_dict:
    if m in season_dict[el] and 0 < m < 13:
        print(f'Month {m} is {el}')

if m in [12, 1, 2]:
    print(f'Month {m} is {season_list[0]}')
elif m in [3, 4, 5]:
    print(f'Month {m} is {season_list[1]}')
elif m in [6, 7, 8]:
    print(f'Month {m} is {season_list[2]}')
elif m in [9, 10, 11]:
    print(f'Month {m} is {season_list[3]}')
else:
    print('There is no month like this')

#Task_4
str = input('Enter a few words (use a space: ').split()
for i, word in enumerate(str, 1):
    print(i, word[:10])

#Task_5
list = [7, 5, 3, 3, 2]
num = int(input('Enter a new number: '))
i = 0
for el in list:
    if num <= el:
        i += 1
list.insert(i, num)

print(list)

#Task_6
params = {'name': "", 'price' : "", 'quantity' : "", 'UOM': ""}
res = {'name': [], 'price' : [], 'quantity' : [], 'UOM': []}
cort = []
i = 0
while True:
    if input('If you want the program to stop, enter "stop"').capitalize() == 'Stop':
        break
    i += 1
    params = params.copy()
    for el in params:
        m = input(f'Enter {el}: ')
        params[el] = int(m) if m == 'price' or m == 'quantity' else m
        res[el].append(params[el])
    cort.append((i, params))
    print(cort)

for key, value in res.items():
    print(f'{key}: {value}')