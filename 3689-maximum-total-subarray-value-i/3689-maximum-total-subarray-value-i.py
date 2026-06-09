class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n=len(nums)
        if n==1:return 0
        elif n==2:
            nums.sort()
            return (nums[-1]-nums[0])*k
        else:
            nums.sort()
            return (nums[-1]-nums[0])*k