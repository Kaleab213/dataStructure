# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        array = []
        while head:
            array.append(head)
            head = head.next
        follow = None
        for i in array:
            head = i
            head.next = follow
            follow = i
        return head



