# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        stack = []
        dummy = ListNode(0)
        dummy.next = head
        temp = dummy
        pos = 0
        prev = None
        after = None

        while pos+1 <left:
            temp = temp.next
            pos+=1
        prev= temp
        temp = temp.next
        for i in range(right-left + 1):
            stack.append(temp)
            temp = temp.next
        after = temp
        temp = prev
        for i in range(right-left + 1):
            curr = stack.pop()
            curr.next =None
            temp.next = curr
            temp = temp.next
        temp.next = after
        return dummy.next
        


            
            
            

        