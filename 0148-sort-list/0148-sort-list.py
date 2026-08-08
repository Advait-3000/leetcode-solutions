# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        val=[]
        while temp:
            val.append(temp.val)
            temp=temp.next
        dummy=ListNode()
        curr=dummy
        val.sort()
        for i in val:
            curr.next=ListNode(i)
            curr=curr.next
        return dummy.next