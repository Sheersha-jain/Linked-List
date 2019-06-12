# Find the length of loop if loop exists

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

    def loopDetection(self):
        loop_found = 0
        slow_pointer = self.head
        fast_pointer = self.head
        while(slow_pointer and fast_pointer and fast_pointer.next):
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if(slow_pointer == fast_pointer):
                loop_found += 1
                break
        if(loop_found ==1):
            self.loopLength(slow_pointer)


    def loopLength(self, loop_node):
        length = 0
        fast_pointer = self.head
        while(loop_node != fast_pointer):
            fast_pointer = fast_pointer.next
            length +=1
        print("length of loop is", length)

llist = Linkedlist()
llist.push(10)
llist.push(4)
llist.push(15)
llist.push(20)
llist.push(50)
llist.head.next.next.next.next.next = llist.head.next.next
llist.loopDetection()
