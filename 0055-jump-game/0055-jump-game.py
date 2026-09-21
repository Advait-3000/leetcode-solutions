class Solution:
    def canJump(self, nums: list[int]) -> bool:
        maxPos=0
        n=len(nums)
        for i, num in enumerate(nums):
            if i>maxPos:return False
            maxPos=max(maxPos,i+num)
        return True