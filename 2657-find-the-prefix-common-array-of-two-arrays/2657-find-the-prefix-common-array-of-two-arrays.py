class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen = set()
        res=[]
        for i in range(len(A)):
            seen.add(A[i])
            seen.add(B[i])
            res.append((i+1)*2-len(seen))
        return res