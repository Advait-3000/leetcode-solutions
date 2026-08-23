class Solution:
    def sumGame(self, num: str) -> bool:
        n=len(num)//2
        sumLeft=sum([int(i) for i in num[:n] if i!='?'])
        sumRight=sum([int(i) for i in num[n:] if i!='?'])
        countLeft=num[:n].count('?')
        countRight=num[n:].count('?')
        return 2*(sumLeft-sumRight)!=9*(countRight-countLeft)