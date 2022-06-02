from timeit import timeit


def format_concate():
    param = 123
    string = "first " + str(param) + " second"


def format_percent():
    param = 123
    string = "first %s second" % param


def format_format():
    param = 123
    string = "first {} second".format(param)


# читаемость и поддерживаемость
def format_f():
    param = 123
    string = f"first {param} second"


print(timeit("format_concate()", "from __main__ import format_concate"))

print(timeit("format_percent()", "from __main__ import format_percent"))

print(timeit("format_format()", "from __main__ import format_format"))

print(timeit("format_f()", "from __main__ import format_f"))

"""
0.33543220000000007
0.31619379999999997
0.37685690000000016
0.22341030000000006
"""
def lst_func():
    import random
    lst = [x for x in range(100)]
    if random.randint(5, 1000) in lst:
        return True
    else:
        return False

def set_func():
    import random
    my_set = (x for x in range(100))
    if random.randint(5, 1000) in my_set:
        return True
    else:
        return False

# print(timeit("lst_func()", "from __main__ import lst_func"))
# print(timeit("set_func()", "from __main__ import set_func"))
from functools import lru_cache

@lru_cache()
def fibo(n):
    if n <=1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

def memorize(f):
    cache = {}
    def decorate (*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorate

@memorize
def fibo1(n):
    if n <=1:
        return 1
    else:
        return fibo1(n-1) + fibo1(n-2)

def memorize(f):
    cache = {}
    def decorate (*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorate

print(timeit("fibo(20)", "from __main__ import fibo"))
print(timeit("fibo1(20)", "from __main__ import fibo1"))