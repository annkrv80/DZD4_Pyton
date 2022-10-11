#Вычислить число c заданной точностью d
from cmath import pi
import os
def clear(): return os.system('cls')


clear()
d = int(input('Введите количество десятичных знаков: '))
print(round(pi, d))
