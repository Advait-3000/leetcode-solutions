class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        early=float('inf')
        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                if landStartTime[i]<waterStartTime[j]:
                    curr=landStartTime[i]+landDuration[i]
                    if curr>=waterStartTime[j]:curr+=waterDuration[j]
                    else: curr=waterStartTime[j]+waterDuration[j]
                elif waterStartTime[j]<landStartTime[i]:
                    curr=waterStartTime[j]+waterDuration[j]
                    if curr>=landStartTime[i]:curr+=landDuration[i]
                    else: curr=landStartTime[i]+landDuration[i]
                else:curr=landStartTime[i]+landDuration[i]+waterDuration[j]
                early=min(early,curr)
        return early