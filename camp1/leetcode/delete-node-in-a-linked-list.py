# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        tempo = node.next
        node.val = tempo.val
        node.next = node.next.next
        tempo.next = None
        

        