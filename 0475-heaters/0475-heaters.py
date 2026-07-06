class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        maxDist = 0
        for house in houses:
            idx = bisect.bisect_left(heaters, house)
            if idx < len(heaters) and heaters[idx] == house:continue
            dist_left = float('inf')
            dist_right = float('inf')
            if idx > 0:dist_left = house - heaters[idx - 1]
            if idx < len(heaters):dist_right = heaters[idx] - house
            maxDist = max(maxDist, min(dist_left, dist_right))
        return maxDist