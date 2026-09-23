class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target=sum(nums)-x
        if target==0:return len(nums)
        if target<0:return -1
        n=len(nums)
        curr=0
        i=0
        max_len=-1
        for j in range(n):
            curr+=nums[j]
            while curr>target and i<=j:
                curr-=nums[i]
                i+=1
            if curr==target:max_len=max(j-i+1,max_len)
        return n-max_len if max_len!=-1 else -1
        