#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
#многочлена и записать в файл многочлен степени k.
import os
from random import randint
clear=lambda:os.system('cls')
clear()

def create_coefficients(n):
    coef = [randint(0, 100) for i in range(n + 1)]
    return coef

def create_polymom(coeffic):
       k = len(coeffic)-1
       polynom = ' '
       for i in range(0,len(coeffic)):
              if i == len(coeffic)-1:
                     polynom+=f'{coeffic[i]}'
              elif k==1:
                     polynom+=f'{coeffic[i]}X + '
              else:
                     polynom+=f'{coeffic[i]}X^{k} + '
              k-=1
       polynom+=' =0'
       return polynom


k = int(input('Введите натуральную степень k '))
coefficients1 = create_coefficients(k)
polynom1 = create_polymom(coefficients1)
print(polynom1)
coefficients2 = create_coefficients(k)
polynom2 = create_polymom(coefficients2)
print(polynom2)

with open ('file1.txt','w') as data:
       data.write(polynom1)
with open ('file2.txt','w') as data:
       data.write(polynom2)

