class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[1]*n
        fix=1
        for i in range(n):
            res[i]=fix
            fix*=nums[i]
        fix=1
        for i in range(n-1,-1,-1):
            res[i]*=fix
            fix*=nums[i]
        return res