class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        que1 = deque()
        que2 = deque()
        for i in range(len(senate)):
            if senate[i] == "R":
                que1.append(i)
            else:
                que2.append(i)
        while que1 and que2:
            if que1[0] < que2[0]:
                que2.popleft()
                que1.append(que1.popleft()+n)
            else:
                que1.popleft()
                que2.append(que2.popleft()+n)
        if que1:
            return "Radiant"
        return "Dire"
