class Node:
    def __init__(self, value):
        self.data = value
        self.next_pointer = None

class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.head.next_pointer = self.tail
        self.tail.next_pointer = self.head

    def insertAthead(self, new_data):
        new_node = Node(new_data)

        if self.head.data is None:
            self.head = new_node
            self.tail = new_node
            new_node.next_pointer = self.head

        temp = self.head
        new_node.next_pointer = temp
        self.head = new_node
        self.tail.next_pointer = self.head


    def printList(self):
        while(self.head):
            print(self.head.data)
            self.head = self.head.next_pointer

list = Linkedlist()
list.head = Node(1)
A = Node(2)
B = Node(3)
C = Node(4)
D = Node(5)
list.head.previous_pointer = None
list.head.next_pointer = A
A.previous_pointer = list.head
A.next_pointer = B
B.previous_pointer = A
B.next_pointer = C
C.previous_pointer = B
C.next_pointer = D
D.previous_pointer = C
D.next_pointer = None
list.insertAttail(66)
list.printList()