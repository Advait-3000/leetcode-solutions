class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        waviness=0
        for num in range(num1,num2+1):
            curr=str(num)
            n=len(curr)
            if n<3:continue
            for i in range(1,n-1):
                if int(curr[i-1])<int(curr[i])>int(curr[i+1]) or int(curr[i-1])>int(curr[i])<int(curr[i+1]):
                    waviness+=1
        return waviness