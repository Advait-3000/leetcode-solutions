class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        mn,mx=nums.index(min(nums)),nums.index(max(nums))
        mn,mx=min(mn,mx),max(mn,mx)
        n=len(nums)
        return min(mx+1,n-mn,mn+1+n-mx)