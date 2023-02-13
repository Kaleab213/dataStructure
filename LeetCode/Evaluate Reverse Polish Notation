class Solution:
    def evalRPN(self, expression: List[str]) -> int:
        def calculate(operator, operand1, operand2):
            sign1, sign2 = 1, 1
            if operand1 < 0:
                sign1 = -1
            if operand2 < 0:
                sign2 = -1
            if operator == '+':
                return operand1 + operand2
            elif operator == '-':
                return operand1 - operand2
            elif operator == '*':
                return operand1 * operand2
            elif operator == '/':
                return floor(abs(operand1) / abs(operand2)) * (sign1 * sign2)
        numbers = []
        for token in expression:
            if token.isdigit() or (len(token) > 1):
                numbers.append(int(token))
            else:
                op1 = numbers.pop()
                op2 = numbers.pop()
                numbers.append(calculate(token, op2, op1))
        return numbers[0]
