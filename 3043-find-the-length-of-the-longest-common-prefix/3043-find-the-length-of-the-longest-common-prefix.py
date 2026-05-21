class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefix=set()
        for i in arr2:
            while i:
                prefix.add(i)
                i//=10
        res=0
        for i in arr1:
            while i:
                if i in prefix:
                    res=max(res,len(str(i)))
                    break
                i//=10
        return res