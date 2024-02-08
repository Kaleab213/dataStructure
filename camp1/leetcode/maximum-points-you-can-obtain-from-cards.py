class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints)
        tempo = sum(cardPoints[:len(cardPoints)-k])
        res = total - tempo
        i = 1
        j = len(cardPoints)-k
        while j<len(cardPoints):
            tempo -= cardPoints[i-1]
            tempo += cardPoints[j]
            res = max(res, total-tempo)
            i += 1
            j += 1
        return res
