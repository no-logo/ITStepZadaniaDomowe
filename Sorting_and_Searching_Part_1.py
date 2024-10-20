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

rand_list = [random.randint(0,100) for i in range(20)]

print(rand_list)
sorted_rand_list = bubble_sort(rand_list)
print(sorted_rand_list)