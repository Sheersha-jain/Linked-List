class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def insertionAtfront(self, new_data):
        if self.head is None:
            print("linked list is empty !!!")
            return
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertionAtlast(self, new_data):
        if self.head is None:
            print("linked list is empty !!!")
            return
        new_node = Node(new_data)
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node

    def insertionAtnode(self, new_data, previous_node):
        if previous_node is None:
            print("position not present !!!")
            return
        k=0
        new_node = Node(new_data)
        current_node = self.head
        while(current_node is not None and k<previous_node):
            current_node = current_node.next
            k +=1

        new_node.next = current_node.next
        current_node.next = new_node

    def printList(self):
        while(self.head):
            print(self.head.data)
            self.head=self.head.next

list = Linkedlist()
list.head = Node(1)
second = Node(2)
third = Node(39)
list.head.next = second
second.next = third
list.insertionAtfront(234)
list.insertionAtfront(789)
list.insertionAtlast(77)
list.insertionAtnode(22,2)
list.insertionAtnode(44,2)
list.insertionAtnode(7,1)
list.printList()