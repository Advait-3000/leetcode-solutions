class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n=len(nums)
        digitSum = []
        for i, num in enumerate(nums):
            d_sum = sum(int(digit) for digit in str(num))
            digitSum.append((d_sum, num, i))
        digitSum.sort(key=lambda x: (x[0], x[1]))       
        visited = [False] * n
        swaps = 0
        for i in range(n):
            if visited[i] or digitSum[i][2] == i:continue
            cycle_size=0
            curr=i
            while not visited[curr]:
                visited[curr] = True
                curr = digitSum[curr][2]
                cycle_size += 1
            if cycle_size > 1:swaps += cycle_size - 1
        return swaps