#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
#многочлена и записать в файл многочлен степени k.
import itertools
import os
from random import randint
def clear(): return os.system('cls')


clear()
k = int(input('Введите натуральную степень k '))
coefficients = [randint(0, 100) for i in range(k + 1)]
print(coefficients)


def create_polynom(sp):
    list = sp[::-1]
    polynom = ''
    if len(list) < 1:
        polynom = 'x = 0'
    else:
        for i in range(len(list)):
            if i != len(list) - 1 and list[i] != 0 and i != len(list) - 2:
                polynom += f'{list[i]}x^{len(list)-i-1}'
                if list[i+1] != 0:
                    polynom += ' + '
            elif i == len(list) - 2 and list[i] != 0:
                polynom += f'{list[i]}x'
                if list[i+1] != 0:
                    polynom += ' + '
            elif i == len(list) - 1 and list[i] != 0:
                polynom += f'{list[i]} = 0'
            elif i == len(list) - 1 and list[i] == 0:
                polynom += ' = 0'
    return polynom


polynom1 = create_polynom(coefficients)
print(polynom1)

k = int(input('Введите натуральную степень k '))
coefficients = [randint(0, 100) for i in range(k + 1)]
print(coefficients)
polynom2 = create_polynom(coefficients)
print(polynom2)

with open('file1.txt', 'w') as data:
    data.write(polynom1)
with open('file2.txt', 'w') as data:
    data.write(polynom2)
