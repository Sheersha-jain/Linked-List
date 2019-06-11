import gc
class Node:
    def __init__(self, value):
        self.data = value
        self.next_pointer = None
        self.previous_pointer = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def deleteHeadnode(self):
        if self.head is None:
            print("Linked list is empty !!!")
            return
        flush = self.head
        self.head =self.head.next_pointer
        self.head.previous_pointer = None
        flush.previous_pointer = None

    def deleteTailnode(self):
        if self.head is None:
            print("linked list is empty !!!")
            return
        temp = self.head
        while(temp.next_pointer is not None):
            temp = temp.next_pointer
        temp.previous_pointer.next_pointer = None
        temp.previous_pointer = None
        del(temp)
        gc.collect()

    def deleteAtnode(self, position):
        current_node = 0
        temp = self.head
        while(temp.next_pointer is not None and current_node<position):
            temp = temp.next_pointer
            current_node = current_node+1
        temp2 = temp.previous_pointer
        temp2.next_pointer = temp.next_pointer
        if(temp.next_pointer):
            temp.next_pointer.previous_pointer = temp2
            del(temp)
            gc.collect()
            return

    def printList(self):
        while(self.head is not None):
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
B.next_pointer =C
C.previous_pointer = B
C.next_pointer = D
D.previous_pointer = C
D.next_pointer = None
list.deleteHeadnode()
list.deleteTailnode()
#list.deleteAtnode(2)
list.printList()