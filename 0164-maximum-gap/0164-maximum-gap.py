class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        n=len(nums)
        if n==1:return 0
        nums.sort()
        diff=0
        for i in range(1,n):
            diff=max(diff,nums[i]-nums[i-1])
        return diff