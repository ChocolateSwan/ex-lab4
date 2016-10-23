#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data = ['Aaa','aaa', 'b', 'B']
data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)
d=[]

# Реализация задания 2
print('Unique с массивом : ')
for i in Unique(data1):
    print(i,end=' ')
print('\nUnique с генератором : ')
for i in Unique(gen_random(1, 4, 100)):
    print(i,end=' ')
print('\nUnique с масивом букв и ignore_case=True : ')
for i in Unique(data,ignore_case = True):
    print(i,end=' ')


