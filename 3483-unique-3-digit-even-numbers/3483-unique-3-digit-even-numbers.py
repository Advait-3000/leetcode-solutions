class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        freq=Counter(digits)
        count=0
        for i in range(100,999,2):
            curr={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
            curr[i%10]+=1
            curr[(i//10)%10]+=1
            curr[(i//100)%10]+=1
            done=True
            for j in curr:
                if curr[j]>freq[j]:done=False
            if done:count+=1
        return count