"""Фибо через рекурсию"""

from timeit import timeit


def func(n_val):
    if n_val < 2:
        return n_val
    return func(n_val - 1) + func(n_val - 2)


n = 8

print(timeit("func(n)", globals=globals()))

"""8.6776222"""
