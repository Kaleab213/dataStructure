class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        left = 0
        right = max(houses[-1], heaters[-1]) - min(houses[0], heaters[0])

        while left < right:
            mid = left + (right - left) // 2
            i = 0  
            for house in houses:
                while i < len(heaters) - 1 and heaters[i] + mid < house:
                    i += 1

                if abs(heaters[i] - house) > mid:
                    left = mid + 1
                    break
            else:
                right = mid

        return left

