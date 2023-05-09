x = int(input("Номер задачи: "))
a = 0
b = 0
c = 0
d = 0


# 4.1
def f1():
    try:
        a = int(input('Введите число: '))
        b = a % 3
    except ValueError:
        print('Введено не число!')
    except ZeroDivisionError:
        print('Введён 0!')
    else:
        if b == 0 and a != 0:
            print('Число', a, 'делится на 3!')
        else:
            print('Число', a, 'не делится на 3!')


if x == 1:
    f1()


# 4.2
def f2():
    try:
        b = int(input('Введите число: '))
        a = 100 / b
    except ValueError:
        print('Введено не число!(')
    except ZeroDivisionError:
        print('Введён 0!Так нельзя >:(')
    else:
        print('100 разделить на введённое число: ', a)


if x == 2:
    f2()


# 4.3
def f3():
    d = int(input('Введите день: '))
    a = int(input('Введите месяц: '))
    b = int(input('Введите год : '))
    b %= 100
    if b == d * a:
        print('Дата магическая!')
        return True
    else:
        print('Дата не является магической!')
        return False


if x == 3:
    f3()


# 4.4
def f4():
    a = 0
    b = 0
    c = input('Введите номер билета: ')
    if len(c) % 2 == 0:
        for i in c[0:int(len(c) / 2)]:
            a += int(i)
        for i in c[int(len(c) / 2):int(len(c)) + 1]:
            b += int(i)
        if a == b:
            print('Билет счастливый!)')
        else:
            print('Билет не является счастливым!(')
    else:
        print('Количество цифр нечётно!(')


if x == 4:
    f4()
if x < 0 or x > 4:
    print("Такой задачи нет(")
