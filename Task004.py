#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
#многочлена и записать в файл многочлен степени k.
import os
from random import randint
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

def polymons(k, file_name):
    coeffic = [randint(0, 100) for i in range(k + 1)]
    res = create_formula(coeffic)
    with open(file_name,'w',encoding='utf-8') as f:
       f.write(' '.join([str(i) for i in coeffic[::-1]]) + '\n')
       f.write(res)

polymons(3,'file1.txt')
polymons(3,'file2.txt')



