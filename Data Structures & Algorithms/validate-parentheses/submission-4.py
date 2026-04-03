class Solution:
    def isMatchingBracket(self, open_bracket: str, close_bracket: str) -> bool:
        match open_bracket:
            case "(":
                return close_bracket == ")"
            case "{":
                return close_bracket == "}"
            case "[":
                return close_bracket == "]"
            case _:
                raise Exception(f"Unexpected bracket - {open_bracket}")

    def isValid(self, s: str) -> bool:
        stack = []
        open_brackets = "({["

        for char in s:
            if char in open_brackets:
                stack.append(char)
            else:
                if not stack or not self.isMatchingBracket(stack[-1], char):
                    return False
                stack.pop(-1)
        
        return not stack