class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        res = 0
        for cost in costs:
            if cost<=coins:
                coins -= cost
                res += 1
            if cost > coins:
                break
        return res
            