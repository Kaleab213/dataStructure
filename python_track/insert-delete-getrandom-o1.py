class RandomizedSet:

    def __init__(self):
        self.theset  = set()

    def insert(self, val: int) -> bool:
        if val in self.theset:
            return False
        self.theset.add(val)
        return True        

    def remove(self, val: int) -> bool:
        if val not in self.theset:
            return False
        self.theset.remove(val)
        return True

    def getRandom(self) -> int:
        idx = random.randint(0, len(self.theset)-1)
        num = 0
        for i in self.theset:
            if num == idx:
                return i
            num+=1



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()