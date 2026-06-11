class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle=[]
        for i in range(numRows):
            n=[]
            if i==0:
                triangle.append([1])
            elif i==1:
                triangle.append([1,1])
            else:
                arr=triangle[len(triangle)-1]
                for j in range(len(arr)):
                    if j==0:
                        n.append(1)
                        n.append(1+arr[1])
                    elif j==len(arr)-1:
                        n.append(1)
                    else:
                        n.append(arr[j]+arr[j+1])
                triangle.append(n)
        return triangle