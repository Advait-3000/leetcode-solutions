class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        occ={}
        for idx, num in enumerate(nums):
            if num in occ:occ[num].append(idx)
            else:occ[num]=[idx]
        for i in occ:
            for j in range(len(occ[i])-1):
                if abs(occ[i][j]-occ[i][j+1])<=k:return True
        return False