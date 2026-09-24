class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n=len(triangle)
        dp=[[0]*i for i in range(1,n+1)]
        dp[0]=triangle[0]
        for i in range(1,n):
            m=len(triangle[i])
            for j in range(m):
                if j==0:dp[i][j]=dp[i-1][j]+triangle[i][j]
                elif j==m-1:dp[i][j]=dp[i-1][j-1]+triangle[i][j]
                else:dp[i][j]=min(dp[i-1][j-1]+triangle[i][j],dp[i-1][j]+triangle[i][j])
        return min(dp[-1])