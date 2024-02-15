class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        store = defaultdict(lambda: 0)
        for bill in bills:
            if bill == 5:
                store[5] += 1
            elif bill == 10:
                if store[5] < 1:
                    return False
                else:
                    store[5] -= 1
                    store[10] += 1
            else:
                if store[10]>=1 and store[5]>=1:
                    store[20] += 1
                    store[10] -= 1
                    store[5] -= 1
                elif store[5]>=3:
                    store[20] += 1
                    store[5] -= 3
                else:
                    return False
        return True
