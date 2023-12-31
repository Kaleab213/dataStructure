class Solution:
    def smallestNumber(self, num: int) -> int:
        num = str(num)
        store = defaultdict(lambda: 0)
        for i in num:
            if i != "-":
                store[i] += 1
        res = ""
        while store:
            if num[0] == "-":
                if not res:
                    res += "-"
                val = max(store)
            else:
                val = min(store)
            res += str(val)*store[val]
            del store[val]
        i = 0
        while i<len(res) and res[i]=="0":
            i += 1
        if i != 0 and i<len(res):
            res = res[i]+res[:i]+res[i+1:]
        return int(res)
        