"""
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.
"""

import hashlib
from collections import Counter

'''
рара

рар
ра
р
а
ар
ара
'''

'''
Сохраняем хэши всех подстрок в множество.
Экономия на размере хранимых данных (для длинных строк) и
скорость доступа вместе с уникальностью элементов,
которые даёт множество, сделают решение коротким и эффективным.
'''

# Вариат 1
s = input("Введите строку из маленьких латинских букв: ")
r = set()

N = len(s)
for i in range(N):
    if i == 0:
        N = len(s) - 1
    else:
        N = len(s)
    for j in range(N, i, -1):
        '''
        возвращается как строковый объект двойной длины, содержащий только
        шестнадцатеричные цифры. Это может использоваться для безопасного
        обмена значениями в электронной почте или других недвоичных средах.
        digest() - набор байтов
        hexdigest() - строка
        '''
        r.add(hashlib.sha1(s[i:j].encode('utf-8')).hexdigest())


print(f"Количество различных подстрок в строке {s} равно {len(r)}")

# Вариат 2
result_set = set()
for sym in range(len(s)):
    last_str = s[sym:]
    for length in range(1, len(last_str) + 1):
        sub_str = s[sym:sym + length]
        if s != sub_str:
            hash_sub_str = hash(sub_str)
            result_set.add(hash_sub_str)

print(len(result_set))

print(f"Количество различных подстрок в строке {s} равно {len(r)}")
