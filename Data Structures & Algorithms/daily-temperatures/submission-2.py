from collections import defaultdict

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # Add tuple (temp, index)
        
        for i, temp in enumerate(temperatures):

            # Only check if stack is not empty
            if stack:
                while stack and (temp > stack[-1][0]):
                    topStackTemp= stack[-1][0]
                    topStackIndex = stack[-1][1]

                    # If temp is warmer than top of stack add difference between the
                    # two indexes to the corresponding top of stack result
                    if temp > topStackTemp:
                        result[topStackIndex] = i - topStackIndex
                        stack.pop()

            stack.append((temp, i))

        return result
            