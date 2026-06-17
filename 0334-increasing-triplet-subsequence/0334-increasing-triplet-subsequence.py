class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i=nums.index(min(nums))
        if not nums[i+1:]:return False
        j=nums.index(min(nums[i+1:]))
        if not nums[j+1:]:return False
        return True