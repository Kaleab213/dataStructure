class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        store = set(arr2)
        res = []
        end = []
        for num in arr2:
            rep = count[num]
            res += [num]*rep
        for num in arr1:
            if num not in store:
                end.append(num)
        end.sort()
        return res+end

        