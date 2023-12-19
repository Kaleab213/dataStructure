class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even = 0
        for num in nums:
            if num%2 == 0:
                even += num

        n = len(queries)
        res = [0]*n
        for i in range(n):
            val, idx = queries[i]
            old = nums[idx]
            nums[idx]+=val
            new = nums[idx]
            if new%2 == 0:
                if old%2 == 0:
                    even += val
                else:
                    even += new
                res[i] = even
            else:
                if old%2 == 0:
                    even -= old
                res[i] = even
        return res
