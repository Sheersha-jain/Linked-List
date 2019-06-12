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
        while(self.head):
            new_node = self.head.next
            print("new_node", new_node.data)
            temp = self.head.next
            print("temp 1", temp.data)
            temp = self.head
            print("temp 2", temp.data)
            self.head = new_node
            print("head data", self.head.data)
            print("next new node", new_node.data)
        print(temp)

llist = Linkedlist()
llist.push(8)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(2)
llist.iterative_reverse()