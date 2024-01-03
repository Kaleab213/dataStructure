class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = []
        for num in range(n, 1, -1):
            idx = arr.index(num)
            res.extend([idx + 1, num])
            arr = arr[:idx:-1] + arr[:idx]
        return res