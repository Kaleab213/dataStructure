class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        ans = 0
        d = {0: 1}
        len_A = len(A)
        acc = 0        
        for i in range(len_A):
            acc += A[i]       
            key = acc % K
            
            if key in d:
                ans += d[key]
                d[key] += 1
            else:
                d[key] = 1
            
        return ans
            