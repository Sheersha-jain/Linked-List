# Given two singly linked list which intersect at some point and become singly link list, the head
# and start pointers of both lists are known but length of both lists are not known
# find the merging point of list

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        curA,curB = headA,headB
        lenA,lenB = 0,0
        while curA is not None:
            lenA += 1
            curA = curA.next
        while curB is not None:
            lenB += 1
            curB = curB.next
        curA,curB = headA,headB
        if lenA > lenB:
            for i in range(lenA-lenB):
                curA = curA.next
        elif lenB > lenA:
            for i in range(lenB-lenA):
                curB = curB.next
        while curB != curA:
            curB = curB.next
            curA = curA.next
        return curA