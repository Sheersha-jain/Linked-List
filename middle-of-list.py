# Find the middle list of linked list.

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def middleNode(self):
        slow_pointer = self.head
        fast_pointer = self.head
        if self.head is not None:
            while(fast_pointer is not None and fast_pointer.next is not None):
                fast_pointer = fast_pointer.next.next
                slow_pointer = slow_pointer.next
            print(slow_pointer.data)

llist = Linkedlist()
llist.push(10)
llist.push(4)
llist.push(15)
llist.push(20)
llist.push(50)
llist.push(78)
llist.push(100)
llist.middleNode()