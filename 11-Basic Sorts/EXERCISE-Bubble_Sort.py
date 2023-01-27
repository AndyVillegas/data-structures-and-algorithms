def bubble_sort(items):
    for j in range(1, len(items) - 1):
        for i in range(len(items) - j):
            if items[i] > items[i + 1]:
                aux = items[i + 1]
                items[i + 1] = items[i]
                items[i] = aux
    return items




print(bubble_sort([4,2,6,5,1,3]))

 

"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
 """