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

    def loopDetect(self):
        slow_pointer = self.head
        fast_pointer = self.head
        loop_found = 0
        while(slow_pointer and fast_pointer and fast_pointer.next):
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if(slow_pointer == fast_pointer):
                loop_found +=1
                break
        if(loop_found ==1):
            slow_pointer = self.head
            while(slow_pointer != fast_pointer):
                slow_pointer = slow_pointer.next
                fast_pointer = fast_pointer.next
                if(slow_pointer == fast_pointer):
                    print("meeting pointer", slow_pointer.data)

llist = Linkedlist()
llist.push(10)
llist.push(4)
llist.push(15)
llist.push(20)
llist.push(50)
llist.head.next.next.next.next.next = llist.head.next.next
llist.loopDetect()