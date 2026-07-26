class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return nums[-1]*nums[-2]*nums[-3] if nums[0]>0 else max(nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3])