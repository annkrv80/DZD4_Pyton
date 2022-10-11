#Задайте последовательность чисел. 
#Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
from itertools import count
import os
from random import randint
clear=lambda: os.system ('cls')
clear()

list = [randint(0, 10) for i in range(5)]
print(list)
list2 = []
count = 0
for i in list:
    for j in list:
        if i == j:
            count += 1
    if count == 1:
        list2.append(i)
    count = 0
print(list2)
