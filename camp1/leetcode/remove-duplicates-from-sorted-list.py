# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        dummy = ListNode()
        dummy.next = head
        while head:
            if head.next != None:
                if head.val == head.next.val:
                    tempo = head.next
                    head.next = head.next.next
                    tempo.next = None
                else:
                    head = head.next
            else:
                head = head.next
        return dummy.next
                