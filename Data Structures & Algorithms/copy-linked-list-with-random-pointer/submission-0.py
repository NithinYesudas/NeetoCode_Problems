"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mem = {}
        temp = head
        dummy = Node(0)
        temp2 = dummy
        while temp:
            newNode = Node(temp.val)
            temp2.next = newNode
            mem[temp] = newNode
            temp = temp.next
            temp2 = temp2.next
        temp = head
        temp2 = dummy.next
        while temp and temp2:
            temp2.random = mem[temp.random] if temp.random is not None else None
            temp2 = temp2.next
            temp = temp.next
        return dummy.next

        