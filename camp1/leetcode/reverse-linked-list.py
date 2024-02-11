# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        self.head = None
        def recursive(node):
            if not node.next:
                self.head = node
                return node

            curr = recursive(node.next)
            curr.next = node
            node.next = None
            return node

        recursive(head)
        return self.head