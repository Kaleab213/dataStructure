class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        res = 0
        falses = deque()
        trues = deque()
        leftt, leftf, right = 0, 0, 0
        while right < len(answerKey):
                if answerKey[right] == "F":
                    if len(falses) == k:
                        res = max(res, right-leftf)
                        leftf = falses.popleft()+1
                    falses.append(right)

                elif answerKey[right] == "T":
                    if len(trues) == k:
                        res = max(res, right-leftt)
                        leftt = trues.popleft()+1
                    trues.append(right)
                right += 1
        res = max(res, right-leftt)
        res = max(res, right-leftf)
        return res
