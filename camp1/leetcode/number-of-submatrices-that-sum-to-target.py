class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        n, m = len(matrix), len(matrix[0])
        count = 0

        # Calculate prefix sums for each row
        for row in matrix:
            for j in range(1, m):
                row[j] += row[j - 1]

        # Iterate over all possible pairs of columns
        for i in range(m):
            for j in range(i, m):
                # Use hashmap to store prefix sums and their frequencies
                prefix_sum_count = {0: 1}
                current_sum = 0
                # Iterate over each row to calculate the sum of submatrices
                for k in range(n):
                    # Calculate the sum of elements between columns i and j in row k
                    current_sum += matrix[k][j] - (matrix[k][i - 1] if i > 0 else 0)
                    # If the difference between the current sum and target exists in prefix_sum_count,
                    # increment the count by the frequency of that difference
                    count += prefix_sum_count.get(current_sum - target, 0)
                    # Update prefix_sum_count with the current sum
                    prefix_sum_count[current_sum] = prefix_sum_count.get(current_sum, 0) + 1

        return count