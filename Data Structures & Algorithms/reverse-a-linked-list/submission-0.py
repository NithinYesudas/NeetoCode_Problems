# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        temp = head
        while temp:
            stack.append(temp)
            temp = temp.next
        dummy = ListNode(0)
        temp = dummy
        while len(stack):
            a = stack.pop()
            a.next = None
            temp.next = a
            temp = temp.next
        return dummy.next

        
        