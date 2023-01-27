
def merge(a, b):
    sorted_list = []
    i = 0
    j = 0
    while i != len(a) and j != len(b):
        if  a[i] < b[j]:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1
    rest = a
    index = i
    if i == len(a):
        rest = b
        index = j
    for n in range(index, len(rest)):
        sorted_list.append(rest[n])
    return sorted_list

def merge(a, b):
    sorted_list = []
    while len(a) != 0 and len(b) != 0:
        if  a[0] < b[0]:
            sorted_list.append(a.pop(0))
        else:
            sorted_list.append(b.pop(0))
    rest = []
    if len(a) == 0:
        rest = b
    else:
        rest = a
    sorted_list.extend(rest)
    return sorted_list

def merge(list1, list2):
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[i])
        j += 1
    return combined

# MERGE REQUIRES TWO SORTED LISTS:
print(merge([1,2,7,8], [3,4,5,6]))



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6, 7, 8]
 """