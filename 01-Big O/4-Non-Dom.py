def print_items(n):
    for i in range(n):
        for j in range(n): # O(n^2)
            print(i,j)

    for k in range(n): # O(n)
        print(k)

print_items(10) # O(n^2 + n)