class Solution:
    def minOperations(self, nums: List[int]) -> int:
        sorted_nums=sorted(nums)
        if nums==sorted_nums:return 0
        reverse=sorted_nums[::-1]
        if nums==reverse:return 1
        n=len(nums)
        idx=nums.index(sorted_nums[0])
        is_sorted_shift=True
        for k in range(n):
            if nums[(idx+k)%n]!=sorted_nums[k]:
                is_sorted_shift=False
                break
        if is_sorted_shift:return min(idx,n-idx+2)
        idx_rev=nums.index(reverse[0])
        is_reverse_shift=True
        for k in range(n):
            if nums[(idx_rev+k)%n]!=reverse[k]:
                is_reverse_shift=False
                break
        if is_reverse_shift:return min(idx_rev, n - idx_rev) + 1
        return -1