class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)
        pre = [0]*n
        for i in range(n):
            if i==0:
                pre[i] = int(s[i])
            if i>0:
                pre[i] = int(s[i])+pre[i-1]
        
        ans=0
        for i in range(1, n-1):
            low = pre[i-1]
            high = pre[n-1]-pre[i]
            if s[i]=='1':
                low = abs(i-low)
                high = abs(n-i-high-1)
            ans+=high*low
        return ans