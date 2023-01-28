def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


def pivot(list, start, end):
    pivot = start
    s = start
    for i in range(start + 1, end + 1):
        if list[pivot] > list[i]:
            s += 1
            swap(list, s, i)
    swap(list, s, pivot)
    return pivot




my_list = [4,6,1,7,3,2,5]

print('List before running pivot():')
print(my_list)

returned_pivot_index = pivot(my_list, 0, 6)

print('\nList after running pivot():')
print(my_list)

print('\nPivot Index:')
print(returned_pivot_index)



"""
    EXPECTED OUTPUT:
    ----------------
    List before running pivot():
    [4, 6, 1, 7, 3, 2, 5]

    List after running pivot():
    [2, 1, 3, 4, 6, 7, 5]

    Pivot Index:
    3

 """