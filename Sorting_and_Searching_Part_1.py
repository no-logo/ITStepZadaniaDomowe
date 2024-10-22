# https://visualgo.net/en/sorting

import random

#1. Bubble sort
print('\n1. Bubble sort\n')

def bubble_sort(slist):
    i = 0
    j = len(slist) - 1
    while i < j and j >= 0:
        if slist[i] > slist[i+1]:
            slist[i], slist[i+1] = slist[i+1], slist[i]
        i += 1
        if i == j and j > 0:
            i = 0
            j -= 1
    return slist

rand_list = [random.randint(0,100) for _ in range(20)]
print(rand_list)
sorted_rand_list = bubble_sort(rand_list)
print(sorted_rand_list)

#2. Selection sort
print('\n2. Selection sort\n')

def selection_sort(slist):
    j = 0
    while j < len(slist):
        min_list_index = j
        min_list_value = slist[j]
        for i in range(j+1, len(slist)):
            if slist[i] < min_list_value:
                min_list_value = slist[i]
                min_list_index = i
        slist[j], slist[min_list_index] = slist[min_list_index], slist[j]
        j += 1

    return slist

rand_list = [random.randint(0,100) for _ in range(20)]
print(rand_list)
sorted_rand_list = selection_sort(rand_list)
print(sorted_rand_list)

#3. Insertion sort
print('\n3. Insertion sort\n')

def insertion_sort(slist):
    j = 0
    while j < len(slist)-1:
        elem_to_insert = slist[j+1]
        for i in range(j, -1, -1):
            if slist[i] > elem_to_insert:
                slist[i+1] = slist[i]
                if i == 0:
                    slist[0] = elem_to_insert
            else:
                slist[i+1] = elem_to_insert
                break
        j += 1
    return slist

rand_list = [random.randint(0,100) for _ in range(20)]

print(rand_list)
sorted_rand_list = insertion_sort(rand_list)
print(sorted_rand_list)

#4. Merge sort
print('\n4. Merge sort\n')

def merge_lists(slist, tmp_list, start, middle, end):
    for i in range(start, end + 1):
        tmp_list[i] = slist[i]

    i = start
    j = middle + 1

    for k in range(start, end + 1):
        if i <= middle:
            if j <= end:
                if tmp_list[j] < tmp_list[i]:
                    slist[k] = tmp_list[j]
                    j += 1
                else:
                    slist[k] = tmp_list[i]
                    i += 1
            else:
                slist[k] = tmp_list[i]
                i += 1
        else:
            slist[k] = tmp_list[j]
            j += 1

    return slist

def merge_sort(slist, tmp_list, start, end):
    if start < end:
        middle = (start + end) // 2
        merge_sort(slist, tmp_list, start, middle)
        merge_sort(slist, tmp_list, middle+1, end)
        slist = merge_lists(slist, tmp_list, start, middle, end)
    return slist

rand_list = [random.randint(0,100) for _ in range(20)]
tmp_list = [0]*len(rand_list)
print(rand_list)
sorted_rand_list = merge_sort(rand_list, tmp_list, 0, len(rand_list) - 1)
print(sorted_rand_list)

#4. Quick sort
print('\n4. Quick sort\n')

def quick_sort(slist, start, end):
    if end <= start:
        return slist
    i = start
    j = end
    tmp_elem = slist[(start + end) // 2]

    while True:
        while tmp_elem > slist[i]:
            i += 1
        while tmp_elem < slist[j]:
            j -= 1
        if i <= j:
            slist[i], slist[j] = slist[j], slist[i]
        else:
            break
    if j > end:
        quick_sort(slist, start, j)
    if i < end:
        quick_sort(slist, i, end)

rand_list = [random.randint(0,100) for _ in range(20)]
print(rand_list)
sorted_rand_list = quick_sort(rand_list, 0, len(rand_list) - 1)
print(sorted_rand_list)
