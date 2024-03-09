class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        if n==1 and intervals[0][0]==intervals[0][1]:
            return [0]
        
        store = defaultdict(lambda: -1)
        for idx in range(n):
            store[intervals[idx][0]] = idx

        res = [-1]*n
        intervals.sort()
        for idx in range(n-1):

            if intervals[idx][0] == intervals[idx][1]:
                res[store[intervals[idx][0]]] = idx
                continue

            left = idx+1
            right = n-1
            while left <= right:

                mid = (left+right)//2
                if intervals[mid][0] >= intervals[idx][1]:
                    right = mid - 1
                else:
                    left = mid + 1

            if left < n and intervals[left][0] >= intervals[idx][1]:
                i = store[intervals[idx][0]]
                res[i] = store[intervals[left][0]]
        return res
