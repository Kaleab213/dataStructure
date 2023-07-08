class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        target = k
        res = 0
        while True:
            tickets[0] -= 1
            res+=1
            if tickets[target] == 0:
                break
            val = tickets.pop(0)
            target -= 1
            if val != 0:
                tickets.append(val)
            if target == -1:
                target = len(tickets)-1
            
        return res
