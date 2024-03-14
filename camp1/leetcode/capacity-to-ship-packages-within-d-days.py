class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def canBeShipped(val):
            count, curr = 0, 0
            for weight in weights:
                if weight > val:
                    return False

                if weight+curr > val:
                    count += 1
                    curr = weight
                else:
                    curr += weight
            return count<days
                
        left, right = max(weights), sum(weights)
        while left<=right:
            mid = (left+right)//2
            if canBeShipped(mid):
                right = mid-1
            else:
                left = mid+1

        return left