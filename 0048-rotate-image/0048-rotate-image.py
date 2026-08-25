class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        copy=[]
        for i in range(n):
            part=[]
            for j in range(n):
                part.append(matrix[j][i])
            copy.append(part[::-1])
        for i in range(n):
            matrix[i]=copy[i]