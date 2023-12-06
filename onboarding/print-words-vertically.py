class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        max_len = 0
        for word in s:
            max_len = max(max_len, len(word))
        res = [""]*max_len
        for idx in range(max_len):
            spaces = ""
            for word in s:
                if idx >= len(word):
                    spaces+=" "
                else:
                    res[idx]+=(spaces+word[idx])
                    spaces = ""
        return res
        