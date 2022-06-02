"""Числа Фибоначчи"""
import sys


sys.setrecursionlimit(10000)


def fib(n, summ):
    if n < 1:
        return summ
    return fib(n-1, summ+n)


c = 4
# c = 998 - уже не работает
# необузданная рекурсия вызывает переполнение стека
print(fib(c, 0))


def fibonacci(n):
    if n <= 1:
        return 1
    else:
        return n + fibonacci(n - 1)

print(fibonacci(4))