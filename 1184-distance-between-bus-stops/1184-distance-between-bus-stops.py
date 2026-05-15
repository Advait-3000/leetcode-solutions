class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        total=sum(distance)
        temp=sum(distance[min(start,destination):max(start,destination)])
        if temp>total//2:return total-temp
        else:return temp