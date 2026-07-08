class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def digitSum(num):
            total=0
            for i in str(num):
                total+=int(i)
            return total
        for idx, num in enumerate(nums):
            if idx==digitSum(num):return idx
        return -1