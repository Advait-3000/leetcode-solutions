class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        def build(starts, durations):
            rides = sorted(zip(starts, durations))
            s = [x for x, _ in rides]
            d = [x for _, x in rides]
            n = len(rides)
            prefixMinDur = [0] * n
            prefixMinDur[0] = d[0]
            for i in range(1, n):
                prefixMinDur[i] = min(prefixMinDur[i - 1], d[i])
            suffixMinFinish = [0] * n
            suffixMinFinish[-1] = s[-1] + d[-1]
            for i in range(n - 2, -1, -1):
                suffixMinFinish[i] = min(suffixMinFinish[i + 1], s[i] + d[i])
            return s, prefixMinDur, suffixMinFinish
        waterS, waterPrefDur, waterSufFinish = build(waterStartTime, waterDuration)
        landS, landPrefDur, landSufFinish = build(landStartTime, landDuration)
        ans = float("inf")
        for s, d in zip(landStartTime, landDuration):
            e = s + d
            idx = bisect_right(waterS, e)
            if idx > 0:ans = min(ans, e + waterPrefDur[idx - 1])
            if idx < len(waterS):ans = min(ans, waterSufFinish[idx])
        for s, d in zip(waterStartTime, waterDuration):
            e = s + d
            idx = bisect_right(landS, e)
            if idx > 0:ans = min(ans, e + landPrefDur[idx - 1])
            if idx < len(landS):ans = min(ans, landSufFinish[idx])
        return ans