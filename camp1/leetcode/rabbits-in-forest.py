class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        store = defaultdict(lambda: 0)
        res = 0
        for answer in answers:
            if store[answer] == 0 or store[answer] > answer:
                res += answer + 1
            store[answer] += 1
            if store[answer] == answer+2:
                store[answer] = 1
        return res