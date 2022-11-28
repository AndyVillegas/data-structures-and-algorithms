class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        pass

    def prepend(self, value):
        pass

    def insert(self, index, value):
        pass

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next



 
my_linked_list = LinkedList(4)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)


"""
    EXPECTED OUTPUT:
    ----------------
    Head: 4
    Tail: 4
    Length: 1
    
"""
my_linked_list.print_list()