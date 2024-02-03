# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head or not head.next:
            return False

        if not head.next.next:
            if head == head.next:
                return True
            return False

        slow = fast = head

        while fast and fast.next and fast.next.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break

        if slow != fast:
            return  False

        return True





