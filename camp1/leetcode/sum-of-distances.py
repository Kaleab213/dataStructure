class Solution:
    def distance(self, nums: List[int]) -> List[int]:

        def helper(store, ps, i, dirn):
            if i<0 or i>=len(nums):
                return ps

            curr = nums[i]
            count = 1

            if curr in store:
                idx, count = store[curr]
                val = ps[idx]
                ps[i] = val+count*(abs(i-idx))
                count += 1

            store[curr] = (i, count)

            i+=1
            if dirn == 'dec': i-=2
            return helper(store, ps, i, dirn)

        n = len(nums)
        forwps = helper({}, [0]*n, 0, 'inc')
        backps = helper({}, [0]*n, n-1, 'dec')

        res = []
        for val1, val2 in zip(forwps, backps):
            res.append(val1+val2)
        return res  