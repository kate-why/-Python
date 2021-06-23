# Task_1
def div(a, b):
    try:
        a, b = int(a), int(b)
        res = a / b
    except ValueError:
        return "Not a number"
    except ZeroDivisionError:
        return "Can't divide by zero"
    return res


num1 = input('Num 1: ')
num2 = input('Num 2: ')
print(div(num1, num2))


# Task_2
def info(name, surname, birth, city, email, tel):
    return f'Name: {name}, Surname: {surname}, Birthday: {birth}, City: {city}, E-mail: {email}, Telephone: {tel}'


print(info(name = input('Name: '),
           surname = input('Surname: '),
           birth = input('Birthday: '),
           city = input('City: '),
           email = input('E-mail: '),
           tel = input('Telephone: ')))


# Task_3
def exc_min(a, b, c):
    try:
        res = sum(sorted([a, b, c])[1:])
        return res
    except TypeError:
        return 'Not a number'


print(exc_min(5, 13, 54))


# Task_4.1
def my_pow(x, y):
    try:
        res = x ** y
        return res
    except TypeError:
        return 'Not a number'


print(my_pow(10, -10))


#Task_4.2
def my_pow2(x, y):
    try:
        x, y = float(x), int(y)
        res = 1
        for i in range(y):
            res /= x
            return round(res, 3)
    except ValueError:
        return 'Not a number'


num1 = input('x: ')
num2 = input('y: ')

print(my_pow2(num1, num2))


#Task_5
def sum():
    res = 0
    while True:
        list = input('Enter values, use a space, type "stop" for exit ').split()
        for num in list:
            if num == 'stop':
                return res
            else:
                try:
                    res += int(num)
                except ValueError:
                    print('Are you tired? Type "exit" or enter a number')
        print('Sum = ', res)


print(sum())


#Task_6
def int_func():
    list = input('Enter your words: ').split()
    for word in list:
        latin = 0
        for i in word:
            if 97 <= ord(i) <= 122:
                latin += 1
        if latin == len(word):
            print(word.title())
        else:
            print(f'Error: "{word}" - only lower case is allowed')


int_func()
