class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n<1000:return str(n)
        s=str(n)
        n=len(s)
        if n%3!=0:s=s[:n%3]+"."+s[n%3:]
        for i in range(s.index(".")+4 if "." in s else 3,n,4):
            s=s[:i]+"."+s[i:]
        return s