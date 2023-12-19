class UndergroundSystem:
    def __init__(self):
        self.averagetime = defaultdict(lambda: [0, 0])
        self.travelling = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.travelling[id] = [stationName, t]
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, time = self.travelling[id]
        val, count = self.averagetime[(start, stationName)]
        self.averagetime[(start, stationName)] = [val+t-time, count+1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        val, count = self.averagetime[(startStation, endStation)]
        return val/count
# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)