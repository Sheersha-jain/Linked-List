# Insert a node in sorted link list.

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

    def sortedInsertion(self, new_data):
        new_node = Node(new_data)
        current = self.head
        while(current is not None and current.data < new_node.data):
            temp = current
            current = current.next
        new_node.next = current
        temp.next = current

    def printList(self):
        while(self.head):
            print(self.head.data)
            self.head = self.head.next

llist = Linkedlist()
llist.push(8)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(2)
llist.sortedInsertion(3)
llist.printList()