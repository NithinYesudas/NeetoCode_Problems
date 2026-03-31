# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0)
        l3 = dummy
        while l1 or l2:
            digitSum = carry
            if l1:
                digitSum+=l1.val
                l1 = l1.next

            if l2:
                digitSum+=l2.val
                l2=l2.next
            carry = 1 if digitSum>9 else 0
            newNode = ListNode(digitSum%10)
            l3.next = newNode
            l3 = l3.next
        if carry:
            l3.next = ListNode(1)
        return dummy.next
        


    
        