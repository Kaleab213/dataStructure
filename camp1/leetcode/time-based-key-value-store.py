class TimeMap:

    def __init__(self):
        self.store = defaultdict(lambda: [])

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        mylist = self.store[key]
        n=len(mylist)

        left = 0
        right = n-1
        while left<=right:

            mid = (left+right)//2
            if mylist[mid][0]>timestamp:
                right = mid-1
            else:
                left = mid+1

        if right>=0 and mylist[right][0]<=timestamp:
            return mylist[right][1]
        return ''

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)