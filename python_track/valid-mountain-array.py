class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3 or arr[1]<=arr[0]:
            return False
        increasing = True
        dirnchange = 0
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                return False
            if arr[i]<arr[i-1] and increasing:
                dirnchange += 1
                increasing = False
            if arr[i]>arr[i-1] and not increasing:
                dirnchange += 1
                increasing = True
            if dirnchange > 1:
                return False
        if dirnchange == 0:
            return False
        return True
