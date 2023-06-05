# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

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
            while array[j] < x and j >0 and array[j-1] >= x:
                array[j-1], array[j] = array[j], array[j-1]
                j-=1
        head = ListNode(array[0])
        current = head
        for i in range(1, len(array)):
            newNode = ListNode(array[i])
            current.next = newNode
            current = current.next
        return head
            

