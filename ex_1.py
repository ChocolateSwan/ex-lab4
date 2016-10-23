#!/usr/bin/env python3
from librip.gens import field,gen_random

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Стелаж', 'price': 7000, 'color': 'white'},
    {'title': 'Вешалка для одежды', 'price': 800, 'color': 'white'}
]
print("Реализация field с одним аргументом :")
for i in field(goods, 'title'):
    print(i,end = ' ')
print("\nРеализация field с двумя аргументами :")
for i in field(goods, 'title', 'price'):
    print(i,end=' ')

print ("\nРеализация gen_random : ",end="")
for i in gen_random(1,10,10):
    print (i,end=' ')


