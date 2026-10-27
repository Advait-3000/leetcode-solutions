class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid=[["#"]*n for i in range(m)]
        i,j=0,0
        while i!=m and j!=n:
            grid[i][j]="."
            if i==j:
                if j==n-1 and i!=m-1:i+=1
                elif j!=n:j+=1
                else:i+=1
            else:
                if i==m-1 and j!=n-1:j+=1
                elif i!=m:i+=1
                else:j+=1
        return ["".join(row) for row in grid]