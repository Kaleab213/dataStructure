class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0
        for col in range(len(strs[0])):
            tempo = []
            for row in range(len(strs)):
                tempo.append(strs[row][col])
            if tempo != sorted(tempo):
                res += 1
        return res
