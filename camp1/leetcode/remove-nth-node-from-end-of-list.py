# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None 

        idx = 0
        fast = ListNode(0, head)
        while fast.next and idx < n:
            fast = fast.next
            idx += 1

        slow = ListNode(0, head)
        while fast.next:
            fast = fast.next
            slow = slow.next

        if slow.next == head:
            head = head.next

        tempo = slow.next
        slow.next = slow.next.next
        tempo.next = None

        return head