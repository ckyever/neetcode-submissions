class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(parenth_string: str, open: int, close: int):
            if open == n and close == n:
                result.append(parenth_string)

            if open != n:
                backtrack(parenth_string + '(', open + 1, close)

            if close != n and open > close:
                backtrack(parenth_string + ')', open, close + 1)

        backtrack("", 0, 0)

        return result