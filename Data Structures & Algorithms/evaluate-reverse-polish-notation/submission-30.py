class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        for tok in tokens:
            match tok:
                case "+":
                    operands.append(operands.pop(-2) + operands.pop(-1))
                case "-":
                    operands.append(operands.pop(-2) - operands.pop(-1))
                case "*":
                    operands.append(operands.pop(-2) * operands.pop(-1))
                case "/":
                    operands.append(int(operands.pop(-2) / operands.pop(-1)))
                case _:
                    operands.append(int(tok))
            
        return operands[0]
            
                    
        