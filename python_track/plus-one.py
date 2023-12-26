class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        sum = ""
        output = []

        for i in digits:
            sum += str(i)

        sum = int(sum)
        sum += 1
        sum = str(sum)
        
        for i in sum:
            output.append(int(i))
        return output
