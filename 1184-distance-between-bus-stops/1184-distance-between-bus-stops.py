class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        temp=sum(distance[min(start,destination):max(start,destination)])
        return min(sum(distance)-temp,temp)