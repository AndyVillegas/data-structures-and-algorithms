def selection_sort(list):
    for i in range(len(list) - 1):
        min_index = i
        for j in range(i + 1, len(list)):
            if list[min_index] > list[j]:
                min_index = j
        if i != min_index:
            aux = list[i]
            list[i] = list[min_index]
            list[min_index] = aux
    return list



print(selection_sort([4,2,6,5,1,3]))

 

"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
 """

