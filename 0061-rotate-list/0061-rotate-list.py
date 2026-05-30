# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        val=[]
        while head:
            val.append(head)
            head=head.next
        if val==[]:return None
        for i in range(k%len(val)):
            val.insert(0, val.pop())
        for i in range(len(val)-1):
            val[i].next=val[i+1]
        val[-1].next=None
        return val[0]