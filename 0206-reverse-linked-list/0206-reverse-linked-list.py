# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        val=[]
        while temp:
            val.append(temp.val)
            temp=temp.next
        temp=head
        while temp:
            temp.val=val.pop()
            temp=temp.next
        return head