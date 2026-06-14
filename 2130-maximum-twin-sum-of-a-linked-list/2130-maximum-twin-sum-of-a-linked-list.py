# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        temp=head
        val=[]
        while temp:
            val.append(temp.val)
            temp=temp.next
        maxSum=val[0]+val[-1]
        i,j=1,len(val)-2
        while i<j:
            if val[i]+val[j]>maxSum:maxSum=val[i]+val[j]
            i+=1
            j-=1
        return maxSum