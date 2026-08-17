class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if nums==sorted(nums)[::-1]:
            nums.sort()
            return
        pivot=None
        for i in range(len(nums)-1,-1,-1):
            if nums[i-1] < nums[i]:
                pivot=i-1
                break
        swap=None
        for i in range(pivot,len(nums)):
            if nums[i]>nums[pivot]:swap=i
        temp=nums[pivot]
        nums[pivot]=nums[swap]
        nums[swap]=temp
        nums[pivot+1:] = sorted(nums[pivot+1:])