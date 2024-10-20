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
print('\n2. Sorting list\n')

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
# https://visualgo.net/en/sorting