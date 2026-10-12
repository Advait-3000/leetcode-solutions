class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        bit_counts = [0] * 31
        for x in nums:
            for i in range(31):
                if (x >> i) & 1:bit_counts[i] += 1
        final_nums = [0] * k
        for i in range(31):
            count = bit_counts[i]
            for j in range(min(count, k)):
                final_nums[j] |= (1 << i)
        ans = sum(x * x for x in final_nums) % (10**9 + 7)
        return ans