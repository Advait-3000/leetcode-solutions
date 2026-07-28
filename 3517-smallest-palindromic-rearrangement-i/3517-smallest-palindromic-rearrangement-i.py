class Solution:
    def smallestPalindrome(self, s: str) -> str:
        s=list(s)
        mid=len(s)//2
        return "".join(sorted(s[:mid]))+s[mid]+"".join(sorted(s[:mid])[::-1]) if len(s)%2==1 else "".join(sorted(s[:mid]))+"".join(sorted(s[:mid])[::-1])