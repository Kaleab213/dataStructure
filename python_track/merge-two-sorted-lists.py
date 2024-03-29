# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        tempo = dummy
        while list1 and list2:
                if list1.val <= list2.val:
                    tempo.next = list1
                    list1 = list1.next
                else:
                    tempo.next = list2
                    list2 = list2.next
                tempo = tempo.next
        if list1 and not list2:
                tempo.next = list1
        else:
                tempo.next = list2
        return dummy.next
            