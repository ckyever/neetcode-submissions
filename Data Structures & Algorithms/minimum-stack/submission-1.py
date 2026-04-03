class MinStack:

    def __init__(self):
        self.stack = []
        self.minimumHash = {}
        

    def push(self, val: int) -> None:
        currentStackLen = len(self.stack)
        if currentStackLen == 0:
            # Bottom element in the stack, so it must be the min value
            self.minimumHash[1] = val
        else:
            previousMin = self.minimumHash[currentStackLen]
            self.minimumHash[currentStackLen + 1] = min(previousMin, val)

        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        # Check what the minimum hash would be for the stack for it's current length
        return self.minimumHash[len(self.stack)]

        
