class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        order="123456789"
        res=[]
        for i in range(len(str(low)), len(str(high))+1):
            x,y=0,i
            while y<=9:
                if low<=int(order[x:y])<=high:res.append(int(order[x:y]))
                x+=1
                y+=1
        return res