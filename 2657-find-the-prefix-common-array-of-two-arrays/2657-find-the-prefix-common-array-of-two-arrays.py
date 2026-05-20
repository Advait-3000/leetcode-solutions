class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        return  [(i+1)*2-len(set(A[:i+1]+B[:i+1])) for i in range(len(A))]