class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        t=0
        while k in range(len(tickets)):
            if k==0 and tickets[k]==1:break
            if tickets[0]==1:tickets.pop(0)
            else:tickets.append(tickets.pop(0)-1)
            k=len(tickets)-1 if k==0 else k-1
            t+=1
        return t+1