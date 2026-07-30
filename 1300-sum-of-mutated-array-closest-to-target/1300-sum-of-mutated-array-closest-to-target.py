class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        left, right = 0, max(arr)
        while left<right:
            mid=(left+right)//2
            if sum(min(x, mid) for x in arr)<target:left=mid+1
            else:right=mid
        sumLeft=sum(min(x, left) for x in arr)
        sumPrev=sum(min(x, left-1) for x in arr)
        return left-1 if abs(target-sumPrev)<=abs(target-sumLeft) else left