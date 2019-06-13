# Template of single link list

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

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


list = Linkedlist()
list.head = Node(1)
second = Node(2)
third = Node(39)
fourth = Node(66)
list.head.next = second
second.next = third
third.next = fourth
