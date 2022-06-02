new_lst = [1, 2, 3]
def new_func():
    #new_lst = [1, 2, 3]
    new_lst.append(new_lst)
    return new_lst


print(new_func())

import sys

print(sys.getsizeof(new_func()))
