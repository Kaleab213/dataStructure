class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        fir = 0
        sec = 0
        res = []
        while fir<len(firstList) and sec<len(secondList):
            small = max(firstList[fir][0], secondList[sec][0])
            big = min(firstList[fir][1], secondList[sec][1])
            if small <= big:
                res.append([small, big])
            if firstList[fir][1] < secondList[sec][1]:
                fir += 1
            else: 
                sec += 1
        return res
        