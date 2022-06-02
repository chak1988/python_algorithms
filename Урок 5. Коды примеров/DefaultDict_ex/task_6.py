"""Класс collections.defaultdict()"""

from collections import defaultdict

LST = [('yellow', 3), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
DEF_DICT = defaultdict(list)
print(DEF_DICT)
for k, v in LST:
    DEF_DICT[k].append(v)

print(DEF_DICT)
print(DEF_DICT.items())
print(sorted(DEF_DICT.items()))
print(DEF_DICT['yellow'])
