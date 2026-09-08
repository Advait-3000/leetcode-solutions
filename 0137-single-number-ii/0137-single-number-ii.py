class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0,len(nums),3):
            if i!=len(nums)-1 and nums[i]!=nums[i+1]:return nums[i]
        return nums[-1]