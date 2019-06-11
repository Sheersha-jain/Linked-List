class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

        # Given a reference to the head of a list and a key,

    # delete the first occurence of key in linked list
    def deleteNode(self, key):

        # Store head node
        temp = self.head

        # If head node itself holds the key to be deleted
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return

        while (temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if (temp == None):
            return
        prev.next = temp.next
        temp = None

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)

print("Created Linked List: ")
llist.printList()
llist.deleteNode(1)
print("\nLinked List after Deletion of 1:")
llist.printList()