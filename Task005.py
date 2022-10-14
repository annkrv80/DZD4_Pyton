#Даны два файла, в каждом из которых находится запись многочлена.
#Задача - сформировать файл, содержащий сумму многочленов.
import os
clear=lambda:os.system('cls')
clear()


def create_formula(coeffic):
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


with open('file1.txt') as f1, open ('file2.txt') as f2:
    polynom1 = [int(i) for i in f1.readline().split()]
    polynom2 = [int(i) for i in f2.readline().split()]
if len(polynom1) == len(polynom2):
    res = [a + b for a, b in zip(polynom1, polynom2)]
elif len(polynom1) > len(polynom2):
    res = polynom1.copy
    for i in range(len(polynom2)):
        res[i] += polynom2[i]
else:
    res = polynom2.copy
    for i in range(len(polynom1)):
        res[i] += polynom1[i]
with open('resuit.txt', 'w') as f:
    f.write(create_formula(res[::-1]))
