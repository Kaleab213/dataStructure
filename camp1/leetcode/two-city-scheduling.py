class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        store = []
        for idx in range(len(costs)):
            diff = abs(costs[idx][0]-costs[idx][1])
            store.append((diff, idx))
        store.sort()

        cityA = []
        cityB = []
        for idx in range(len(costs)-1, -1, -1):
            val, i = store[idx]
            if len(cityA) == len(costs)/2:
                cityB.append(costs[i][1])
            elif len(cityB) == len(costs)/2:
                cityA.append(costs[i][0])
            else:
                _, i = store[idx] 
                if costs[i][0] < costs[i][1]:
                    cityA.append(costs[i][0])
                else:
                    cityB.append(costs[i][1])
        
        res = 0
        for val1, val2 in zip(cityA, cityB):
            res += val1+val2
        return res
