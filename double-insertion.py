class Node:
    def __init__(self, value):
        self.data = value
        self.next_pointer = None
        self.previous_pointer = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def insertionAthead(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            new_node.previous_pointer = None
            return
        new_node.previous_pointer = None
        new_node.next_pointer = self.head
        self.head.previous_pointer = new_node
        self.head = new_node

    def insertAtend(self, new_data):
        new_node = Node(new_data)
        temp = self.head
        if self.head is None:
            new_node.previous_pointer = None
            self.head = new_node
            return

        while(temp.next_pointer is not None):
            temp = temp.next_pointer
        temp.next_pointer = new_node
        new_node.previous_pointer = temp
        new_node.next_pointer = None

    def insertAtindex(self, new_data, position):
        current_node = 0
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            new_node.previous_pointer = None
            return
        temp = self.head
        while(temp.next_pointer is not None and current_node < position):
            temp = temp.next_pointer
            current_node = current_node+1
        flush = temp.next_pointer
        temp.next_pointer = new_node
        new_node.next_pointer = temp
        new_node.next_pointer = flush


    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next_pointer

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
B.next_pointer =C
C.previous_pointer = B
C.next_pointer = D
D.previous_pointer = C
D.next_pointer = None
list.insertionAthead(44)
list.insertAtend(66)
list.insertAtindex(78, 2)
list.printList()
