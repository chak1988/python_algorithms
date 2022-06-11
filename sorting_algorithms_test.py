def buble_sort(list_to_sort):
    swapped = True
    while swapped:
        swapped = False
        for x in range(len(list_to_sort) - 1):
            if list_to_sort[x] > list_to_sort[x + 1]:
                list_to_sort[x], list_to_sort[x + 1] = list_to_sort[x + 1], list_to_sort[x]
                swapped = True

    return  list_to_sort

lst = [0, 1, 33, 6, -2, 1, 0]

print(buble_sort(lst))

import random

def quick_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list

    elem = random.choice(unsorted_list)

    left = list(filter(lambda x: x < elem, unsorted_list))
    right = list(filter(lambda x: x > elem, unsorted_list))
    center = [ x for x in unsorted_list if x == elem]

    return quick_sort(left) + center + quick_sort(right)

lst2 = [90, 23, 4, 0, 0, 5, 2, 9, 1]

print(quick_sort(lst2))

a = 20

b = 40
b2 = 60
c2 = 70
d2 =00

from flask import Flask, render_template

app = Flask(__name__)

lst_name = {'Anton': 33, 'Julia': 38, 'Ivan' : 7}

@app.route('/hello')
def hello():
    return render_template('page_1.html', person = lst_name)

if __name__=='__main__':
    app.run(debug = True, port = 8000)