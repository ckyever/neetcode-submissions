class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        calculateStack = []
        for token in tokens:
            print(token)
            try:
                calculateStack.append(int(token))
            except:
                # Number at the top of the stack will be the first number to use or the running total
                print("stack before=" + str(calculateStack))

                total = calculateStack.pop()
                nextNumber = calculateStack.pop()
                print("total=" + str(total))
                print("nextNumber=" + str(nextNumber))

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
            
                print("stack after=" + str(calculateStack))


        # We should only have one number remaining in the calculateStack and that is the final answer
        return calculateStack.pop()




        