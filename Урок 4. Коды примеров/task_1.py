"""Генерация списков"""
from timeit import Timer


# итератор с конкатенацией
def test_concat():
    my_lst = []
    for i in range(1000):
        my_lst = my_lst + [i]


# итератор с функцией append
def test_cycle():
    my_lst = []
    for i in range(1000):
        my_lst.append(i)


# списковое включение
def test_lst_comp():
    my_lst = [i for i in range(1000)]


# встроенная функция range
def test_range():
    my_lst = list(range(1000))


t1 = Timer("test_concat()", "from __main__ import test_concat")
print("list concat ", t1.timeit(number=1000), "milliseconds")

t2 = Timer("test_cycle()", "from __main__ import test_cycle")
print("list append ", t2.timeit(number=1000), "milliseconds")

t3 = Timer("test_lst_comp()", "from __main__ import test_lst_comp")
print("list comprehension ", t3.timeit(number=1000), "milliseconds")

t4 = Timer("test_range()", "from __main__ import test_range")
print("list range ", t4.timeit(number=1000), "milliseconds")

"""
concat  1.1779784 milliseconds
append  0.0715625000000002 milliseconds
comprehension  0.033750200000000063 milliseconds
range  0.011227300000000273 milliseconds

Вы можете объяснить получение таких результатов?
"""
