class Solution:
    def checkValidString(self, s: str) -> bool:
        minOpen,maxOpen=0,0
        for i in s:
            if i=="(":
                minOpen+=1
                maxOpen+=1
            elif i==")":
                minOpen-=1
                maxOpen-=1
            else:
                minOpen-=1
                maxOpen+=1
            if maxOpen<0:return False
            minOpen=max(minOpen,0)
        return minOpen==0
            