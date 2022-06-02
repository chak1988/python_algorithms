"""
Задача 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

from uuid import uuid4
import hashlib

salt = uuid4().hex  # -> 952604f24d9f4cd0b515a39c73657027
cache_obj = {}


def get_page(url):
    if cache_obj.get(url):
        print(f'Данный адрес: {url} присутствует в кэше')
    else:
        res = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        cache_obj[url] = res
        print(cache_obj)


get_page('https://geekbrains.ru/')
get_page('https://geekbrains.ru/')
get_page('https://geekbrains.ru/')

class HashPage:

    salt = uuid4().hex

    def __init__(self):
        self.cache_obj1 = dict()

    def get_page(self, url):
        if self.cache_obj1.get(url):
            return f'Данный адрес: {url} присутствует в кэше'
        else:
            res = hashlib.sha256(self.salt.encode() + url.encode()).hexdigest()
            self.cache_obj1[url] = res
            return self.cache_obj1

a = HashPage()
b = HashPage()
print(a.get_page('https://geekbrains.ru/'))
print(a.get_page('https://geekbrains.ru/'))
print(b.get_page('https://geekbrains.ru/'))
print()
print(a.__dict__)
print(b.__dict__)