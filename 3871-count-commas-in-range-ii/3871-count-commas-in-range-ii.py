class Solution:
    def countCommas(self, n: int) -> int:
        if n==1000000000000000:return 3998998998999005
        elif n>1000000000000:return ((n-1000000000000)*4 + 2998998999004)
        elif n==1000000000000:return 2998998999004
        elif n>1000000000:return ((n-1000000000)*3 + 1998999003)
        elif n==1000000000:return 1998999003
        elif n>1000000:return ((n-1000000)*2 + 999002)
        elif n==1000000:return 999002
        else:return max(0,n-999)