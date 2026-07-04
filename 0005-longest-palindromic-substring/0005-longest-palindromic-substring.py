class Solution:
    def longestPalindrome(self, s: str) -> str:
        ls=""
        lls=0
        n=len(s)
        for i in range(n):
            j=n
            while i<j:
                ss=s[i:j]
                lss=len(ss)
                if ss==ss[::-1]:
                    if lss>lls:
                        ls=ss
                        lls=lss
                    break
                j-=1
        return ls