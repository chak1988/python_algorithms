"""Профилировка затрат памяти"""

import copy
from memory_profiler import profile, memory_usage
from sys import getrefcount

# ссылки, поэтому gc не запускается
@profile
def function_1():
    """Выделяет доп память, не освобождается"""
    x = list(range(100000))
    y = copy.deepcopy(x)
    return y


@profile
def function_2():
    """Выделяет доп память, освобождается"""
    x = list(range(100000))
    print(getrefcount(x))
    y = copy.deepcopy(x)
    print(getrefcount(y))
    del x
    y = None
    return y


if __name__ == "__main__":
    function_1()
    function_2()
