"""Примеры с md5"""

import hashlib

hash_obj = hashlib.md5(b'Testing md5 func')
print(hash_obj)  # -> <md5 HASH object @ 0x0000021C4B589A20>
print(type(hash_obj))  # -> <class '_hashlib.HASH'>
res = hash_obj.hexdigest()
print(type(res))  # -> <class 'str'>
print(res)  # -> b631e4f1254574b9c386fcbc9145d0c3 == b631e4f1254574b9c386fcbc9145d0c3

print()
hash_obj_2 = hashlib.md5(("Тестируем функцию md5").encode('utf-8'))
print(hash_obj_2)  # -> <md5 HASH object @ 0x0000021C4D53ED50>
print(type(hash_obj_2))  # -> <class '_hashlib.HASH'>
res_2 = hash_obj_2.hexdigest()
print(type(res_2))  # -> <class 'str'>
print(res_2)  # -> cb63de18e7c52d17e3b5e9743210ab74
