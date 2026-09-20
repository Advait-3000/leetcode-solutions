class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum((i+1)*(27-ord(s[i])+ord('a')-1) for i in range(len(s)))