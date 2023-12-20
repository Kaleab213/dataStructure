class Solution(object):
    def findDiagonalOrder(self, matrix):
        d=defaultdict(lambda: [])
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                d[i+j].append(matrix[i][j])

        ans = []
        for entry in d.items():
            print(entry)
            if entry[0]%2 == 0:
                [ans.append(x) for x in entry[1][::-1]]
            else:
                [ans.append(x) for x in entry[1]]
        return ans
