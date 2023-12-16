class OrderedStream:

    def __init__(self, n: int):
        self.store = {}
        self.idx = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        res = []
        self.store[idKey] = value
        while self.idx in self.store:
            res.append(self.store[self.idx])
            del self.store[self.idx]
            self.idx+=1
        return res

        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)