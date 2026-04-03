from collections import defaultdict

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # loop through temperatures
            # if stack is empty add it
            # else if temp is > top stack
                # get index of temp and index of top stack and add difference to the result list
                # pop top of stack and keep checking top of stack
                # add to stack
            # temp is <= top stack
                # add to stack
        # for results without number add 0

        result = [0] * len(temperatures)
        stack = [] # Add tuple (temp, index)
        for i, temp in enumerate(temperatures):

            print(f"i={i} temp={temp}")
            print(f"stack={stack}")
            # Only check if stack is not empty
            if stack:
                while stack and (temp > stack[-1][0]):
                    topStackTemp= stack[-1][0]
                    topStackIndex = stack[-1][1]
                    print(f"top stack: temp={topStackTemp} index={topStackIndex}")

                    # If temp is warmer than top of stack add difference between the
                    # two indexes to the corresponding top of stack result
                    if temp > topStackTemp:
                        result[topStackIndex] = i - topStackIndex
                        stack.pop()
                        print(f"result={result}")
                        print(f"stack={stack}")


            stack.append((temp, i))

        return result
            