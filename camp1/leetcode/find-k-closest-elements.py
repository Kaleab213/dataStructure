class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        smallest = []
        difference = []
        for i in range(len(arr)):
            if len(smallest) < k:
                smallest.append(arr[i])
                difference.append(abs(arr[i]-x))
            else:
                if difference[0] > difference[-1]:
                    idx = 0
                    amt = difference[0]
                else:
                    idx = -1
                    amt = difference[-1]
                if abs(arr[i]-x) < amt:
                    smallest.pop(idx)
                    difference.pop(idx)
                    smallest.append(arr[i])
                    difference.append(abs(arr[i]-x))
        return smallest

                
