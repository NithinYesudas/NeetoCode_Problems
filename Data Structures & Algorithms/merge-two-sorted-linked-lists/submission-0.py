# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        temp = dummy
        p1 = list1
        p2 = list2
        while p1 and p2:
            if p1.val <= p2.val:
                temp.next = p1
                p1 = p1.next
            else:
                temp.next = p2
                p2 = p2.next
            temp = temp.next
        if p1:
            temp.next = p1
        else:
            temp.next = p2
        return dummy.next

        