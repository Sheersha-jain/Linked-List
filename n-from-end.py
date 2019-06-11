# Find the nth node from the end of linked list. (Brute-force-method)

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def printList(self):
        while(self.head):
            self.head = self.head.next

    def nNodefromend(self, number):
        length = 0
        temp = self.head
        while(temp is not None):
            temp = temp.next
            length += 1

        if number > length:
            print("location is not present in the list")
            return
        temp = self.head
        for i in range(0, length-number):
            temp = temp.next
        print(temp.data)

    def n_nodeusingPointers(self, number):
        count = 0
        temp1 = self.head
        temp2 = None
        for i in  range(count, number):
            if(temp1):
                temp1 = temp1.next
                count += 1
        while(temp1):
            if(temp2 is None):
                temp2 = self.head
            temp2 = temp2.next
            temp1 = temp1.next
        if(temp2):
            print(temp2.data)
        return None


list = Linkedlist()
list.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)
sixth = Node(6)
list.head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = sixth
list.nNodefromend(1)
list.n_nodeusingPointers(3)
list.printList()