class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        store = set()
        for i, j in ranges:
            for k in range(i, j+1):
                store.add(k)
        for i in range(left, right+1):
            if i not in store:
                print(i, store)
                return False
        return True
