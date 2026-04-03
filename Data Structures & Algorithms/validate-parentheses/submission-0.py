class Solution:
    def isValid(self, s: str) -> bool:
        
        # Edge cases
        # "[" = false
        # "()()" = true
        # "({}{})"

        # Time: O(n)  Space: O(n)
        stack = []
        for char in s:
            if char in "({[":
                stack.append(char)

            # This must be a closing bracket
            else:
                if not stack:
                    # Stack is empty so this means first character was a closing bracket so invalid
                    return False

                lastOpenedBracket = stack[len(stack) - 1]

                # Check current closing bracket matches the last opened bracket
                if (char == ")" and lastOpenedBracket == "(") \
                or (char == "}" and lastOpenedBracket == "{") \
                or (char == "]" and lastOpenedBracket == "["):
                    stack.pop()
                else:
                    # Incorrect bracket used to close
                    return False

        # If we still have brackets in the stack this means they have not been closed, therefore the string is invalid
        if stack:
            return False

        return True
