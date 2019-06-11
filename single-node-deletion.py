class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def deleteFrontnode(self, position):

        temp =self.head

        if temp is None:
            print("list is empty !!!")
        if position ==0:
            self.head = temp.next
            temp =None

    def deleteLastnode(self):
        if self.head is None:
            print("list is empty !!!")
        temp = self.head


    def deleteAtnode(self, position):
        pass
            

    def printList(self):
        while(self.head):
            print(self.head.data)
            self.head = self.head.next

list = Linkedlist()
list.head = Node(1)
second = Node(2)
third = Node(55)
fourth = Node(77)
fifth = Node(88)
sixth = Node(99)
list.head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next =sixth

list.deleteFrontnode(0)
list.deleteAtnode(2)
list.printList()


