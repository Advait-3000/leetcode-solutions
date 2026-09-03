class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        return True if min(nums1)%2==1 else len(set([i%2 for i in nums1]))==1