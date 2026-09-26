class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        know={}
        for i in knowledge:
            know[i[0]]=i[1]
        while "(" in s:
            left=s.index("(")
            right=s.index(")")
            if s[left+1:right] in know:s=s[:left]+know[s[left+1:right]]+s[right+1:]
            else:s=s[:left]+"?"+s[right+1:]
        return s