class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n=len(temperatures)
        ans=[0]*n
        stack=[]
        for idx,temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<temp:
                prev_index=stack.pop()
                ans[prev_index]=idx-prev_index
            stack.append(idx)
        return ans