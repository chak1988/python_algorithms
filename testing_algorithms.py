from timeit import timeit

def func_2(nums):
    """O(n) – линейная сложность"""
    return [i for i, el in enumerate(nums) if el % 2 == 0]


print(func_2([20, 30, 40, 2, 4, 1, 0, 7]))


def recursive_reverse(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'

print(recursive_reverse(12345))

def recursion(num):
    if num == 0:
        return ''
    else:
        return f'{str(num%10)}{recursion(num//10)}'

print(recursion(1233645723542634987534685))

def memorize (f):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return wrapper

@memorize
def recursion1(num):
    if num == 0:
        return ''
    else:
        return f'{str(num%10)}{recursion(num//10)}'

print(timeit('recursion(1233645723542634987534685)', 'from __main__ import recursion', number = 10))
print(timeit('recursion1(1233645723542634987534685)', 'from __main__ import recursion1', number = 20))
print(timeit('recursion1(1233645723542634987534685)',  globals = globals()))

import random
array = [random.randint(0,10) for i in range(10)]

def func_3():
    numb = max(array, key=array.count)
    return f"Чаще всего встречается число {numb}, оно появилось в массиве {array.count(numb)} раз(а)"

print(func_3())