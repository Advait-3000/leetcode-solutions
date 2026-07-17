class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        total=0
        for i in range(k):
            total+=(happiness.pop()-i)
        return total