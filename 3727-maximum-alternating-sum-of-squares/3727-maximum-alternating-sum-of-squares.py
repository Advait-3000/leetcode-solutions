class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums=sorted(num*num for num in nums)
        minus=False
        count=0
        while nums:
            if minus:count-=nums.pop(0)
            else:count+=nums.pop()
            minus=not minus
        return count