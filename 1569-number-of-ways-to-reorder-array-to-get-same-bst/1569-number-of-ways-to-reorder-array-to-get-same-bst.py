class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        def solve(nums):
            n=len(nums)
            if n==0 or n==1:return 1
            leftTree,rightTree=[],[]
            root=nums[0]
            for i in range(1,n):
                if nums[i]<root:leftTree.append(nums[i])
                else:rightTree.append(nums[i])
            l=len(leftTree)
            r=len(rightTree)
            return (math.comb(l+r,l)*solve(leftTree)*solve(rightTree))%(10**9 + 7)
        return solve(nums)-1