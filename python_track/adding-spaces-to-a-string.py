class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ''
        start = 0
        for space in spaces:
            res += s[start: space]
            res += " "
            start = space
        res += s[start: ]
        return res
        