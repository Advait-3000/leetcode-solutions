class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        freq=Counter(nums)
        maxStreak=0
        for num in freq:
            if num-1 not in freq:
                curr=num
                streak=1
                while curr+1 in freq:
                    curr+=1
                    streak+=1
                maxStreak=max(maxStreak, streak)
        return maxStreak