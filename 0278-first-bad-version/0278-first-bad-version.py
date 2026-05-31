# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low,high=0,n
        while low<=high:
            mid=low+(high-low)//2
            if isBadVersion(mid) and isBadVersion(mid-1)==False:return mid
            elif isBadVersion(mid) and isBadVersion(mid-1):high=mid-1
            else:low=mid+1