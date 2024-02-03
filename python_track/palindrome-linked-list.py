# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        array = []
        while head:
            array.append(head.val)
            head = head.next
        j = len(array)-1
        for i in range(len(array)):
            if j < i:
                break
            if array[i] != array[j]:
                return False
            j-=1
        return True

