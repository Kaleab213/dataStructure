class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        store = {}
        for winner, looser in matches:
            if winner not in store:
                store[winner] = 0
            if looser not in store:
                store[looser] = 1
            else:
                store[looser]+=1
        res = [[],[]]
        for player in store:
            if store[player] == 0:
                res[0].append(player)
            elif store[player] == 1:
                res[1].append(player)
        res[0].sort(), res[1].sort()
        return res
        