class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum,rightSum=[],[]
        left,right=0,0
        n=len(nums)
        while len(leftSum)!=n:
            leftSum.append(left)
            left+=nums[len(leftSum)-1]
        while len(rightSum)!=n:
            rightSum.insert(0,right)
            right+=nums[n-len(rightSum)]
        return [max(leftSum[i],rightSum[i])-min(leftSum[i],rightSum[i]) for i in range(n)]