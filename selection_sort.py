
def find_minimum(arr):
    min = arr[0]
    index = 0
    for i in range(1,len(arr)):
        if arr[i] < min:
            min = arr[i]
            index = i
    
    return index

def selection_sort(arr):
    new_arr = []
    for i in range(0,len(arr)):
        index_min = find_minimum(arr)
        new_arr.append(arr.pop(index_min))

    return new_arr


print(selection_sort([12,10,3,16,20,8]))
