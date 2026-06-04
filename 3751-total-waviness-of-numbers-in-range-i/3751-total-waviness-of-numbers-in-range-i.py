waviness=[0]
for num in range(1,1000000):
    curr=str(num)
    n=len(curr)
    if n<3:
        waviness.append(0)
        continue
    waves=0
    for i in range(1,n-1):
        if int(curr[i-1])<int(curr[i])>int(curr[i+1]) or int(curr[i-1])>int(curr[i])<int(curr[i+1]):
            waves+=1
    waviness.append(waves)
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        return sum(waviness[num1:num2+1])