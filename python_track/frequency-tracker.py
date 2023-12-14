class FrequencyTracker:

    def __init__(self):
        self.mydict = defaultdict(lambda: 0)
        self.mydict2 = defaultdict(lambda: set())

    def add(self, number: int) -> None:
        freq = self.mydict[number]
        if self.mydict[number]>0:
            self.mydict2[freq].remove(number)
        self.mydict2[freq+1].add(number)
        self.mydict[number]+=1

    def deleteOne(self, number: int) -> None:
        if self.mydict[number] > 0:
            freq = self.mydict[number]
            self.mydict2[freq].remove(number)
            if freq > 1:
                self.mydict2[freq-1].add(number)
            self.mydict[number]-=1

    def hasFrequency(self, frequency: int) -> bool:
        if len(self.mydict2[frequency])>0:
            return True
        return False
        
# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)