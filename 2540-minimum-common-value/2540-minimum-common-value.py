class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        if set(nums1).intersection(set(nums2)):
            return min(set(nums1).intersection(set(nums2)))
        else:
            return -1