# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp=[]
        while list1:
            temp.append(list1)
            list1=list1.next
        while list2:
            temp.append(list2)
            list2=list2.next
        if not temp:return None
        temp.sort(key=lambda x: x.val)
        for i in range(len(temp)-1):
            temp[i].next = temp[i+1]
        return temp[0] 