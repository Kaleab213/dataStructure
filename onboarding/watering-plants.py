class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        src = capacity
        step = 0
        for idx in range(len(plants)):
            if plants[idx] > capacity:
                capacity = (src-plants[idx])
                step += (idx*2)
            else:
                capacity-=plants[idx]
            step += 1
        return step
