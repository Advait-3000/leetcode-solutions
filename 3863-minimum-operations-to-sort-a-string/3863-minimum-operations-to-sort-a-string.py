class Solution:
    def minOperations(self, s: str) -> int:
        if s=="".join(sorted(s)):return 0
        elif len(s)==2:return -1
        mn,mx=min(s),max(s)
        if s[0]==mn or s[-1]==mx:return 1
        elif any(c==mn or c==mx for c in s[1:-1]):return 2
        else:return 3