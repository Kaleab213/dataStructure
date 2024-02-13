# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None
        if not head.next:
            return head

        array = []
        while head:
            array.append(head.val)
            head = head.next

        for i in range(len(array)-1):
            j = i + 1
            while j > 0 and array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
                j-=1

        head = ListNode(array[0])
        current = head
        for i in range(1,len(array)):
            new_node = ListNode(array[i])
            current.next = new_node
            current = new_node
        return head

        