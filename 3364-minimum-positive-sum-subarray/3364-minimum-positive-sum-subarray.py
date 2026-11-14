class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        curr=float('inf')
        n=len(nums)
        for l in range(l,r+1):
            for i in range(n-l+1):
                total=sum(nums[i:i+l])
                if total>0 and total<curr:curr=total
        return curr if curr!=float('inf') else -1