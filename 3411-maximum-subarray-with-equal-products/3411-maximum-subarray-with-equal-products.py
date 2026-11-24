class Solution:
    def prod(self, nums: List[int]) -> int:
        prod=1
        for num in nums:
            prod*=num
        return prod
    def maxLength(self, nums: List[int]) -> int:
        n=len(nums)
        for j in range(n,1,-1):
            for i in range(n-j+1):
                if self.prod(nums[i:i+j])==math.gcd(*nums[i:i+j])*math.lcm(*nums[i:i+j]):return j