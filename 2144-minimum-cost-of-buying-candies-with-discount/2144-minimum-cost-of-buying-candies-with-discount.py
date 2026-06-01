class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        expence=0
        for i in range(1,len(cost)+1):
            if i%3==0:cost.pop()
            else:expence+=cost.pop()
        return expence