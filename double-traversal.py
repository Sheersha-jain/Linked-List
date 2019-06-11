class Node:
    def __init__(self, value):
        self.data = value
        self.next_pointer = None
        self.previous_pointer = None

class Linkedlist:

    def __init__(self):
        self.head = None

    def traverseList(self):
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
list.traverseList()