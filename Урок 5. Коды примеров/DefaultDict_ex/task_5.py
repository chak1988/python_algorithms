"""Класс collections.defaultdict()"""
from collections import defaultdict

d = defaultdict(str)
d['раз'] = 'раз'
d['два'] = 'два'
print(d['три'])  # -> defaultdict(<class 'str'>, {'раз': 'раз', 'два': 'два'})

dict_of_lst = defaultdict(list)
for k in range(7):
    dict_of_lst[k].append(k)
print(dict_of_lst)  # -> defaultdict(<class 'list'>, {0: [0], 1: [1], 2: [2], 3: [3], 4: [4], 5: [5], 6: [6]})
