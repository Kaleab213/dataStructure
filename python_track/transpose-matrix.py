class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []
        for col in range(len(matrix[0])):
            tempo = []
            for row in range(len(matrix)):
                tempo.append(matrix[row][col])
            res.append(tempo)
        return res

        