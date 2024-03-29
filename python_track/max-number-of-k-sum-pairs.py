class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = {}
        operations = 0
        for num in nums:
            if (k - num) in count and count[k-num] > 0:
                operations += 1
                count[k-num] -= 1
            else:
                count[num] = count.get(num, 0) + 1
        return operations