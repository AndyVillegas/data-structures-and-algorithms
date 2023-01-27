def insertion_sort(list):
    for i in range(1, len(list)):
        temp = list[i]
        j = i - 1
        while temp < list[j] and j > -1:
            list[j + 1] = list[j]
            list[j] = temp
            j -= 1
    return list




print(insertion_sort([4,2,6,5,1,3]))



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
 """

