"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
Рекурсия вам нужна для решения левой части выражения.
Полученный результат нужно просто сравнить с результатом в правой.

Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2

Подсказка:
В ф-цию принимаются два элемент - это левая и правая части

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def recur_method(numb):
    if numb == 1:
        return numb
    else:
        return recur_method(numb - 1) + numb


try:
    NUMB = int(input("Введите число: "))
    if recur_method(NUMB) == NUMB * (NUMB + 1) / 2:
        print('Равенство верно')
except ValueError:
    print("Вы вместо числа ввели строку (((. Исправьтесь")
