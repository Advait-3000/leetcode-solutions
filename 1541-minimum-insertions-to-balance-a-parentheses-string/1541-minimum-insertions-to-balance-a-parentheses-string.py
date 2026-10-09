class Solution:
    def minInsertions(self, s: str) -> int:
        s=list(s)
        i=0
        count=0
        brac=0
        while i in range(len(s)-1):
            if s[i]==")" and s[i+1]==")":
                s[i]="))"
                s.pop(i+1)
            i+=1
        for i in s:
            if i=="(":brac+=1
            elif i=="))" and brac:brac-=1
            elif i==")" and brac:
                count+=1
                brac-=1
            elif i==")":count+=2
            else:count+=1
        return count+(brac)*2