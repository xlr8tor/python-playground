import math
def quicksort(list):
    if len(list) < 2:
        return list
    else:
        pivot = list[len(list)//2]
        less = [i for i in list if i <= pivot]
        greater = [i for i in list if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([2,3,12,1,9,5,10]))