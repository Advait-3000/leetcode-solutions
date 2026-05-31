# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        size=0
        while temp:
            size+=1
            temp=temp.next
        temp=head
        if size==n:return head.next
        for i in range(size-n-1):
            temp=temp.next
        if temp.next==None:return None
        temp.next=temp.next.next
        return head