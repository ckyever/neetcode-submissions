class Solution:
    def isValid(self, s: str) -> bool:
        bracket_match = {"(": ")", "{": "}", "[": "]"}
        stack = []
        open_brackets = "({["

        for char in s:
            if char in open_brackets:
                stack.append(char)
            else:
                if not stack or bracket_match.get(stack[-1]) != char:
                    return False
                stack.pop(-1)
        
        return not stack