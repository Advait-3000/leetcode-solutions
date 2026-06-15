# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:return None
        temp=head
        size=0
        while temp:
            size+=1
            temp=temp.next
        mid=size//2
        temp=head
        for i in range(mid-1):
            temp=temp.next
        temp.next=temp.next.next
        return head