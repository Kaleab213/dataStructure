# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        current = dummy

        while list1 or list2:
            if not list1 and list2:
                current.next = list2
                break
            elif not list2 and list1:
                current.next = list1
                break
            elif list1.val > list2.val:
                current.next = list2
                list2 = list2.next
                current = current.next
            else:
                current.next = list1
                list1 = list1.next
                current = current.next

        return dummy.next
        