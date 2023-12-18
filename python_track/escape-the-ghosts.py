class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        ghost_max = float('inf')
        for ghost in ghosts:
            ghost_time = abs(ghost[0]-target[0])+abs(ghost[1]-target[1])
            ghost_max = min(ghost_max, ghost_time)
        distance = abs(target[0])+abs(target[1])
        return distance < ghost_max
    