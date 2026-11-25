class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:return n
        BASE1, MOD1 = 100003, 1_000_000_007
        BASE2, MOD2 = 100019, 1_000_000_009
        def has_unique(length: int) -> bool:
            if length == n:return True
            pow1 = pow(BASE1, length - 1, MOD1)
            pow2 = pow(BASE2, length - 1, MOD2)
            h1 = 0
            h2 = 0
            for i in range(length):
                val = nums[i]
                h1 = (h1 * BASE1 + val) % MOD1
                h2 = (h2 * BASE2 + val) % MOD2
            freq = defaultdict(int)
            freq[(h1, h2)] += 1
            for i in range(1, n - length + 1):
                out_val = nums[i - 1]
                in_val = nums[i + length - 1]
                h1 = ((h1 - out_val * pow1) * BASE1 + in_val) % MOD1
                h2 = ((h2 - out_val * pow2) * BASE2 + in_val) % MOD2
                freq[(h1, h2)] += 1
            return any(count == 1 for count in freq.values())
        lo, hi = 1, n
        ans = n
        while lo <= hi:
            mid = (lo + hi) // 2
            if has_unique(mid):
                ans = mid
                hi = mid - 1
            else:lo = mid + 1
        return ans