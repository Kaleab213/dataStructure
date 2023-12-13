class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        val = float('inf')
        res = []
        for word in list1:
            if word in list2:
                idx1 = list1.index(word)
                idx2 = list2.index(word)
                if idx1+idx2 < val:
                    res = [word]
                    val = idx1+idx2
                elif idx1+idx2 == val:
                    res.append(word)
                    val = idx1+idx2
        return res


        