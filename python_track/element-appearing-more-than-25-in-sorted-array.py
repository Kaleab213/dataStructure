class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count = Counter(arr)
        maxpresent = 0
        res = 0
        for val, rep in count.items():
            if rep > maxpresent:
                maxpresent = rep
                res = val
        return res

        