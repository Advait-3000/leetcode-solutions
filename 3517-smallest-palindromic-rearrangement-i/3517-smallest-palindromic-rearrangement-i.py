class Solution:
    def smallestPalindrome(self, s: str) -> str:
        s=list(s)
        n=len(s)
        first=s[:n//2]
        first.sort()
        return "".join(first)+s[n//2]+"".join(first[::-1]) if n%2==1 else "".join(first)+"".join(first[::-1])