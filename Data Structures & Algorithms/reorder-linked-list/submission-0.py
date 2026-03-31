# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        mem = []
        temp = head
        while temp:
            mem.append(temp)
            temp = temp.next
        left = 0
        right = len(mem)-1
        dummy =  ListNode(0)
        temp = dummy
        count = 0
        while left<=right:
            if count%2==0:
                temp.next = mem[left]
                
                left+=1
            else:
                temp.next = mem[right]
                right-=1
            temp = temp.next
            temp.next = None
            count+=1
        head = dummy.next

        
        

            


        