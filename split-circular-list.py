# Split a circular linked list from mid.

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def push(self, data):
        ptr1 = Node(data)
        temp = self.head

        ptr1.next = self.head
        if self.head is not None:
            while (temp.next != self.head):
                temp = temp.next
            temp.next = ptr1

        else:
            ptr1.next = ptr1

        self.head = ptr1

    def printList(self):
        temp = self.head
        if self.head is not None:
            while (True):
                print
                "%d" % (temp.data),
                temp = temp.next
                if (temp == self.head):
                    break

    def splitList(self, head1, head2):
        slow_pointer = self.head
        fast_pointer = self.head
        if self.head is None:
            return
        while(fast_pointer is not None and fast_pointer.next is not None):
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        if(fast_pointer.next.next == self.head):
            fast_pointer = fast_pointer.next

        head1.head = self.head
        if(self.head.next is not self.head):
            head2.head = slow_pointer
        fast_pointer.next = slow_pointer.next
        slow_pointer.next = self.head


    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next


