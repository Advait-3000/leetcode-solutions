# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp=head
        seen=[]
        while temp:
            if temp.next in seen:return True
            else:seen.append(temp.next)
            temp = temp.next
        return False