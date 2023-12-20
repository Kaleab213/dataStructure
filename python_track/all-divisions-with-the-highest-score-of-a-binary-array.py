class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            if nums[0] == 1:
                return [0]
            return [1]
        totalcount = Counter(nums)
        idxcount = defaultdict(lambda: 0)
        zeros = 0
        for i in range(n):
            idxcount[i] = zeros
            if nums[i] == 0:
                zeros += 1
        idxcount[n] = totalcount[0]
       
        res = []
        top = 0
        for idx in idxcount:
            leftsum = idxcount[idx]
            rightsum = (n-idx) - (totalcount[0]-idxcount[idx])
            if leftsum+rightsum > top:
                res = [idx]
                top = leftsum+rightsum
            elif leftsum+rightsum == top:
                res.append(idx)
        return res

        

            
        