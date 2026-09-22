class Solution:
    def jump(self, nums: list[int]) -> int:
        n=len(nums)
        dp=[float('inf')]*n
        dp[0]=0
        for i, num in enumerate(nums):
            for j in range(num):
                if i+j+1<n:dp[i+j+1]=min(dp[i]+1,dp[i+j+1])
        return dp[-1]