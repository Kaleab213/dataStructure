class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        def rec(index):
            if index == 0:
                array = [1]
                return array
            elif index == 1: 
                array = [1,1]
                return array

            array = rec(index - 1)
            tempo = []
            for i in range(len(array)-1):
                tempo.append(array[i] + array[i+1])
            tempo = tempo[::-1]
            array = [1,1]
            for i in tempo:
                array.insert(1, i)
            return array

        return rec(rowIndex)
