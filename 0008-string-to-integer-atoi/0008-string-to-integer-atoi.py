class Solution:
    def myAtoi(self, s: str) -> int:
        n=""
        for i in s:
            if n=="" and (i=="-" or i=="+"):n+=i
            elif i.isdigit():n+=i
            elif n=="" and i==" ":continue
            else:break
        if n=="" or n=="-" or n=="+":return 0
        elif int(n)<=-2**31:return -2**31
        elif int(n)>=(2**31)-1:return (2**31)-1
        return int(n)
        

