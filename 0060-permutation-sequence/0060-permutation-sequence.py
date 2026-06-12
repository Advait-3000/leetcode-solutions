class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1, n + 1)]
        k -= 1  # convert to 0-based indexing
        ans = []

        while nums:
            f = math.factorial(len(nums) - 1)
            idx = k // f
            ans.append(nums.pop(idx))
            k %= f

        return "".join(ans)