class Solution:
    def sortSentence(self, s: str) -> str:
        value = ""
        x = s.split()
        dic = {}
        for i in x:
            dic[i[-1]] = i[:-1]
        for j in sorted(dic):
            value += dic[j]
            if j == list(sorted(dic))[-1]:
                return value
            value += " "
        return value