"""
Теперь воспользуемся формулой (n*(n+1))/2
"""

import time


def check_3(n):

    start_val = time.time()

    end_val = time.time()

    return (n*(n+1))/2, end_val - start_val


print(check_3(10))


for i in range(5):
    print(f'Операция заняла {check_3(10000)[1]} сек')

"""
Стоит обратить внимание, что какое бы значение n мы не передали в функцию,
итоговое время окажется экстремальном малым

Намного эффективнее других вариантов, не правда ли?

Давайте выявим некоторые особенности первых двух решений.
1) Они итеративные, а такие решения из-за повторения некоторого набора шагов потребуют больше времени.
2) Также мы заметили, что время итеративного решения увеличивается с ростом входного значения n

Вроде все понятно. Нужно использовать третий вариант. Но и здесь оказывается не все так просто.
Если запустить третью ф-цию на разных машинах или реализовать алгоритм этой ф-ции на других языках программирования,
то результаты скорее всего не будут идентичными. Чем старше будет машина, тем больше потребуется времени.


Теперь понятно, что получать оценку времени в цифровом выражении не так уж хорошо
Ведь это время зависит от конкретной машины, программы, времени дня, компилятора и языка программирования.
Было бы хорошо подобрать характеристику, не зависящую от этих параметров, 
но дающую понятные результаты.

Чтобы мы могли бы применить эту характеристику для оценки алгоритма самого по себе
и сравнения одного алгоритма с другими.
"""
