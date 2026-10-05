class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        s=list(s.replace("()","1"))
        for i in range(len(s)):
            if s[i]=="1":s[i]=1
        while len(s)!=1:
            i=0
            while i in range(len(s)-1):
                if s[i]!="(" and s[i]!=")":
                    if s[i-1]=="(" and s[i+1]==")":s=s[:i-1]+[s[i]*2]+s[i+2:]
                    elif s[i+1]!="(" and s[i+1]!=")":s=s[:i]+[s[i]+s[i+1]]+s[i+2:]
                    else:i+=1
                else:i+=1
        return s[0]