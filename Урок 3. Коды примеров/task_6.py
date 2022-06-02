"""Хеширование и соль"""

# Модуль uuid применяется для генерации случайного числа
from uuid import uuid4
import hashlib

salt = uuid4().hex  # -> 6a1e300f48c54b77a7ef4af58376a95c
print(salt)

passwd = "programmer"
# соль идет дополнительно к хешу
res = hashlib.sha256(salt.encode() + passwd.encode()).hexdigest() + ':' + salt  #  -> 022cf2d005a201ab60
# 5658a3345dcfaef7a8bfe050efa7c671b3754e91f1e9bb:6a1e300f48c54b77a7ef4af58376a95c
print(res)
