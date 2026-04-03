class Solution:
    def isValid(self, s: str) -> bool:
        bracket_match = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            if char in bracket_match:
                if stack and bracket_match.get(char) == stack[-1]:
                    stack.pop(-1)
                else:
                    return False
            else:
                stack.append(char)
        
        return not stack