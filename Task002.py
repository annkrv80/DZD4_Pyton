#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
import os
def clear(): return os.system('cls')


clear()

n = int(input('Введите число N: '))
d = 2
list = []
while d**2 <= n:
    if n % d == 0:
        list.append(d)
        n = n//d
    else:
        d += 1
list.append(n)
print(list)
