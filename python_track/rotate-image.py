class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        j = n-1

        for i in range(n//2):
            matrix[i], matrix[j] = matrix[j], matrix[i]
            j -= 1

        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        return matrix


