class Solution:
    def squareSum(self, n: int) -> int:
        ans=0
        while n>0:
            ans+=(n%10)**2
            n//=10
        return ans
    def isHappy(self, n: int) -> bool:
        while n>4:
            n=self.squareSum(n)
        return n==1