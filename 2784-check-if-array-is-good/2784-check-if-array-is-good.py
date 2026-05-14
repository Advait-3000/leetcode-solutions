class Solution:
    def isGood(self, nums: List[int]) -> bool:
        og=[i for i in range(1,max(nums)+1)]
        og.append(max(nums))
        nums.sort()
        return nums==og