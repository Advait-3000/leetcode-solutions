class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sortedArr=sorted(set(arr))
        for idx, val in enumerate(arr):
            arr[idx]=bisect.bisect_left(sortedArr, val)+1
        return arr