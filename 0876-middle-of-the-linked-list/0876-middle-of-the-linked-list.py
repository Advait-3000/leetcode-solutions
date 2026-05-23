# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count=0
        temp=head
        while temp:
            count+=1
            temp=temp.next
        middle=count//2
        res=[]
        temp=head
        while head:
            while middle:
                middle-=1
                head=head.next
            res.append(head)
            head=head.next
        for i in range(len(res)-1):
            res[i].next=res[i+1]
        head=res[0]
        return head