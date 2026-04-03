class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        list = []

        # Parentheses string will always start with open 
        list.append("(")

        for i in range(1, n*2):
            j = len(list)
            while j > 0:
                possibleString1 = list[j-1] + "("
                possibleString2 = list[j-1] + ")"
                if self.isValidParenthesesString(possibleString1, n):
                    list[j-1] = possibleString1

                    if self.isValidParenthesesString(possibleString2, n):
                        list.append(possibleString2)

                elif self.isValidParenthesesString(possibleString2, n):
                    list[j-1] = possibleString2
                j -= 1

        return list

    def isValidParenthesesString(self, string: str, n: int) -> bool:
        dict = {"open": 0, "close": 0}
        for parenth in string:
            if parenth == "(":
                dict["open"] += 1
            else: # must be ")"
                dict["close"] += 1

        openCount = dict["open"]
        closeCount = dict["close"]

        return (
            openCount >= closeCount
            and openCount <= n
            and closeCount <= n
        )