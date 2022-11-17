def reverseLL(A):
    if A == None or A.next == None:
        return A
    node = reverseLL(node.next)
    node.next.next = node
    node.next = None
    return node

class LinkedList:
    def __init__(self):
        self.head = None

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

first_node = Node(1)
second_node = Node(2)
third_node = Node(3)

l_list = LinkedList()

l_list.head = first_node
first_node.next = second_node
second_node.next = third_node

print(first_node.data)

print(reverseLL(l_list.head))



