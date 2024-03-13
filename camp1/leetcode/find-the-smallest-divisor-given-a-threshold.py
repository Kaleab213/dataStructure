class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        while left <= right:
            mid = (left+right)//2

            total = 0
            for num in nums:
                total += math.ceil(num/mid)
            
            if total <= threshold:
                right = mid-1
            else:
                left = mid+1
                
        return left