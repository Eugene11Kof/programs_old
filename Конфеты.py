from math import gcd
from functools import reduce
#вводим список конфет
x = input().split()
#выводим в множестве уникальные типы конфет
x_set = set(x)
#создаем список для подсчета каждого типа конфет
amount = []
#считаем количество каждого типа конфет
for i in x_set:
    amount.append(x.count(i))
#ищем наибольший общий делитель - это и есть наш ответ
nod = reduce(gcd, amount)
print(nod)
