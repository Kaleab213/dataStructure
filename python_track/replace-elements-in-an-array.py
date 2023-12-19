class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        store = {}
        for idx, num in enumerate(nums):
            store[num] = idx
        for operation in operations:
            old, new = operation
            idx = store[old]
            nums[idx] = new
            del store[old]
            store[new] = idx
        return nums

        
