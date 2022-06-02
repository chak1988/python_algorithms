"""Класс collections.OrderedDict()"""
from timeit import timeit
from uuid import uuid4
import collections

NEW_DICT = {'a': 1, 'b': 2, 'c': 3}  # -> с версии 3.6 порядок сохранится
print(NEW_DICT)  # -> {'a': 1, 'b': 2, 'c': 3}

# а в версии 3.5 и более ранних можно было получить и такой результат
# {'b': 2, 'c': 3, 'a': 1}
# и вообще любой, ведь порядок ключей не сохранялся

# поэтому приходилось при необходимости обращаться к OrderedDict
NEW_DICT = collections.OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(NEW_DICT)  # -> OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# {} vs OrderedDict ??

usual_dict = {k:v for v, k in enumerate(range(5,20000))}
ordered_dict = collections.OrderedDict({k:v for v, k in enumerate(range(5,200))})
print(timeit('[x for x in usual_dict.values() if x > 6]', globals =globals(), number = 1000))
print(timeit('[x for x in ordered_dict.values() if x > 6]', globals =globals(), number = 1000))