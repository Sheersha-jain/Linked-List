# Check if Linked list is Palindrome.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def __init__(self,seq):
        """prepends item of lists into linked list"""
        self.head = None
        for item in seq:
            node = ListNode(item)
            node.next = self.head
            self.head = node


    def list_palin(self):
        """ Returns 1 if linked list is palindrome else 0"""
        node = self.head
        fast = node
        prev = None
        ispal = True

        # prev approaches to middle of list till fast reaches end or None
        while fast and fast.next:
            fast = fast.next.next
            temp = node.next   #reverse elemets of first half of list
            node.next = prev
            prev = node
            node = temp

        if fast:  # in case of odd num elements
            tail = node.next
            print("tail")
        else:    # in case of even num elements
            tail = node


        while prev and ispal:
            print("prev",prev.val)
            # compare reverse element and next half elements
            if prev.val == tail.val:
                tail = tail.next
                prev = prev.next
                ispal = True
            else:
                ispal = False
                break

        if ispal :
            return 1
        else :
            return 0

# Test Cases
listpal_1 = Solution([7, 8, 6 ,  3 , 7 ,3 , 6, 8, 7])
assert listpal_1.list_palin()
listpal_2 = Solution([6 , 3 , 7, 3, 6])
assert listpal_2.list_palin()
listpal_3 = Solution([3, 7 ,3 ])
assert listpal_3.list_palin()
listpal_4 = Solution([1])
assert listpal_4.list_palin()