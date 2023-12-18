class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        equal = []
        bigger = []
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num == pivot: 
                equal.append(num)
            else:
                bigger.append(num)
        return less+equal+bigger
        