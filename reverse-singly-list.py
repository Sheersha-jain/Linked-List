# Reverse a singly linked list, both iterative and recursive method

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

    def iterative_reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def recursive_reverse(self, current, previous):
        if current is None:
            self.head = current
            current.next = previous
            return
        next = current.next
        current.next = previous
        self.iterative_reverse(next, current)

    def reverse(self):
        if self.head is None:
            return
        self.reverseUtil(self.head, None)

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

llist = Linkedlist()
llist.push(8)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(2)
llist.iterative_reverse()
llist.printList()