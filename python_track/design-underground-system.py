class UndergroundSystem:
    def __init__(self):
        self.averagetime = defaultdict(lambda: [])
        self.travelling = defaultdict(lambda: [])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.travelling[id] = [stationName, t]
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, time = self.travelling[id]
        self.averagetime[start].append([stationName, t-time])

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        mydata = self.averagetime[startStation]
        count = 0
        duration = 0
        for station, time in mydata:
            if station == endStation:
                duration += time
                count += 1
        return duration/count

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)