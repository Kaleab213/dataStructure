class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = blocks[:k].count("W")
        i = 1
        j = k
        tempo = res
        while j<len(blocks):
            if blocks[i-1]=="W" and blocks[j]=="B":
                tempo -= 1
            elif blocks[i-1]=="B" and blocks[j]=="W":
                tempo += 1
            res = min(res, tempo)
            i += 1
            j += 1
        return res
