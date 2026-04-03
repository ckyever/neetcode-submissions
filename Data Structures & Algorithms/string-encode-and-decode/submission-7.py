class Solution:
    delimiter = ":"

    def encode(self, strs: List[str]) -> str:
        code = ""
        for word in strs:
            code += f"{len(word)}{self.delimiter}{word}"
        
        return code


    def decode(self, s: str) -> List[str]:
        strs = []

        word = ""
        lengthString = ""
        countDown = 0

        for char in s:
            # We are decoding a word
            if countDown > 0:
                word += char
                countDown -= 1
                if countDown == 0:
                    # Reached end of word so add to output and clear out word
                    strs.append(word)
                    word = ""

            # We are getting the length of the next word
            else:
                if char == self.delimiter:
                    countDown = int(lengthString)
                    lengthString = ""

                    # If word is just an empty string we still want to make sure we add an empty string to the list
                    if countDown == 0:
                        strs.append("")
                else:
                    lengthString += char

        return strs



