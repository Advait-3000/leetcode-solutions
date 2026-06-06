class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total=sum(nums)
        leftSum=0
        arr=[]
        for pos, val in enumerate(nums):
            arr.append(abs(total-leftSum-val))
            leftSum+=val
            total-=val
        return arr