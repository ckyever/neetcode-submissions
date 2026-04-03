class Node:
    def __init__(self):
        self.children = dict()
        self.is_end_word = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = Node()
            current = current.children[char]
        
        current.is_end_word = True

    def search(self, word: str) -> bool:      
        self.found = False

        def dfs(word: str, current: Node):
            if not word:
                self.found = current.is_end_word
                return
            
            next_char = word[0]
            if next_char == '.':
                for char in current.children.keys():
                    dfs(word[1:], current.children[char])

            else:
                if next_char in current.children:
                    dfs(word[1:], current.children[next_char])
            
        dfs(word, self.root)
        return self.found
        
