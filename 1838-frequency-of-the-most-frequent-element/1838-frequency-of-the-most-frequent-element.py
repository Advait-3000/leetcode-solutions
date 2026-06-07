class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        total=0
        maxLength=1
        n=len(nums)
        nums.sort()
        i=0
        for j in range(n):
            total+=nums[j]
            while nums[j] * (j - i + 1) - total > k:
                total -= nums[i]
                i += 1
            maxLength = max(maxLength, j - i + 1)
        return maxLength