# Given a singly linked list, write a function to swap elements pairwise.
# For example, if the linked list is 1->2->3->4->5 then the function should change
# it to 2->1->4->3->5,

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

    def pairwiseSwap(self):
        temp = self.head
        while(temp is not None and temp.next is not None):
            temp.data , temp.next.data = temp.next.data, temp.data
            temp = temp.next.next

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
list.printList()
print("-----")
list.pairwiseSwap()
print("-----")
list.printList()

