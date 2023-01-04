import math

def binary_search(arr, int):
    start = 0
    end = len(arr) - 1
    result = -1

    for n in range(0,len(arr)):
        pivot = start + math.floor((end - start)/2)
        if arr[pivot] == int:
            result = pivot
            break
        elif arr[pivot] < int:
            start = n + 1
        elif arr[pivot] > int:
            end = n - 1

    return result

print(binary_search([1,2,3,4,5,6,7],0))


