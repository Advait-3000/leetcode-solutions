class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return [sum(1 if nums1[i] in nums2 else 0 for i in range(len(nums1))), sum(1 if nums2[i] in nums1 else 0 for i in range(len(nums2)))]