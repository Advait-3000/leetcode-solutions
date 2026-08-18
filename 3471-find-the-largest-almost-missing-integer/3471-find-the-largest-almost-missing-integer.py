class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        sub=[]
        for i in range(len(nums)-k+1):
            sub.append(nums[i:i+k])
        nums=list(set(nums))
        nums.sort()
        count=1
        num=-1
        for i in nums:
            temp=0
            for j in sub:
                if i in j:temp+=1
            if temp<=count:
                count=temp
                num=i
        return num