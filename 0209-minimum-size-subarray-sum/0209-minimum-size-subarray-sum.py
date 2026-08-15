class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        mn=float('inf')
        i=0
        total=0
        for j in range(len(nums)):
            total+=nums[j]
            while total>=target:
                mn=min(mn,j-i+1)
                total-=nums[i]
                i+=1
        return mn if mn!=float('inf') else 0