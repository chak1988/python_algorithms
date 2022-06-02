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