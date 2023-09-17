class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        val1 = float('inf')
        val2 = float('inf')
        for i in nums:
            if i > val2:
                return True
            if i > val1:
                val2 = min(val2, i)
            val1 = min(val1, i)
        return False
