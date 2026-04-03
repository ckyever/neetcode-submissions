class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        calculateStack = []
        for token in tokens:
            try:
                calculateStack.append(int(token))
            except:
                # Number at the top of the stack will be the first number to use or the running total
                total = calculateStack.pop()
                nextNumber = calculateStack.pop()
                match token:
                    case "+":
                        calculateStack.append(nextNumber + total)
                    case "-":
                        calculateStack.append(nextNumber - total)
                    case "*":
                        calculateStack.append(nextNumber * total)
                    case "/":
                        # Ensure we truncate towards zero
                        calculateStack.append(int(nextNumber/total))

        # We should only have one number remaining in the calculateStack and that is the final answer
        return calculateStack.pop()




        