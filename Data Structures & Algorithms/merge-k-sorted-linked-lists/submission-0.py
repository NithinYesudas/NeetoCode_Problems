# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        output = None
        for i in range(len(lists)-1):
            p1=None
            if output:
                p1 = output
            else:
                p1 = lists[i]
            p2 = lists[i+1]
            dummy = ListNode(0)
            temp = dummy
            while p1 and p2:
                if p1.val <= p2.val:
                    temp.next = p1
                    p1 =p1.next
                else:
                    temp.next = p2
                    p2 = p2.next
                temp = temp.next
            if p1:
                temp.next = p1
            else:
                temp.next = p2
            output = dummy.next
        return output

        