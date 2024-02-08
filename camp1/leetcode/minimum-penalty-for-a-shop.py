class Solution:
    def bestClosingTime(self, customers: str) -> int:
        ps = [0]*len(customers)
        for idx in range(len(customers)):
            if customers[idx] == "Y":
                if idx == 0:
                    ps[idx] = 1
                else:
                    ps[idx] = ps[idx-1]+1
            else:
                if idx == 0:
                    ps[idx] = -1
                else:
                    ps[idx] = ps[idx-1]-1 
        val = max(ps)
        if val<=0:
            return 0
        return ps.index(val)+1
