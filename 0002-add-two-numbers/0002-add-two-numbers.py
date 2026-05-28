# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def to_int(arr):
            out=0
            for i in arr:
                out=out*10 + i
            return out
        num1,num2=[],[]
        while l1:
            num1.append(l1.val)
            l1=l1.next
        while l2:
            num2.append(l2.val)
            l2=l2.next
        arr=list(str(to_int(num1[::-1])+to_int(num2[::-1])))[::-1]
        dummy = ListNode()
        curr = dummy
        for num in arr:
            curr.next = ListNode(int(num))
            curr = curr.next
        return dummy.next