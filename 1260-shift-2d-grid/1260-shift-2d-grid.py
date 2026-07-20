class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        vals=[]
        for i in grid:
            for j in i:
                vals.append(j)
        i=0
        while i<k:
            vals.insert(0,vals.pop())
            i+=1
        new=[]
        m=len(grid[0])
        for i in range(0,len(vals),m):
            new.append(vals[i:i+m])
        return new