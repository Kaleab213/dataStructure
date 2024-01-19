class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        start = 0
        end = len(skill)-1
        chemistry = 0 
        while start < end:
            if skill[start]+skill[end] != skill[0]+skill[-1]:
                return -1
            chemistry += (skill[start]*skill[end])
            start += 1
            end -= 1
        return chemistry


