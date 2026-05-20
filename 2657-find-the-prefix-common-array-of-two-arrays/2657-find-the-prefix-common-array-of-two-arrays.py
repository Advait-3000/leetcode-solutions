class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        return  [len(A[:i+1]+B[:i+1])-len(set(A[:i+1]+B[:i+1])) for i in range(len(A))]