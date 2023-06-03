# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None
            
        odd = head
        even = evenHead = head.next

        while odd.next and even.next:
            odd.next = even.next
            odd = even.next
            even.next = odd.next
            even = odd.next

        odd.next = evenHead
        return head
