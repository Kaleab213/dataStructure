class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        count = [0] * (n + 1)
        for start, end in requests:
            count[start] += 1
            count[end + 1] -= 1
        for i in range(1, n + 1):
            count[i] += count[i - 1]
            
        count.pop() 
        count.sort()
        nums.sort()

        res = 0
        mod = 10**9 + 7
        for num, freq in zip(nums, count):
            res = (res + num * freq) % mod
        return res
                   