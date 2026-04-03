class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        prefix = ""
        encodedString = ""

        for string in strs:
            prefix += f"{len(string)},"
            encodedString += string

        # Remove last unnecessary ','
        prefix = prefix[:-1]

        return f"{prefix}!{encodedString}"


    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []

        bangIndex = s.index("!")
        wordLengths = s[:bangIndex].split(",")
        words = s[bangIndex+1:]

        decodedWords = []
        wordsIndex = 0

        for length in wordLengths:
            currentWord = ""
            print(length)
            for currentWordIndex in range(1, int(length)+1):
                currentWord += words[wordsIndex]
                wordsIndex += 1
            decodedWords.append(currentWord)


        return decodedWords
