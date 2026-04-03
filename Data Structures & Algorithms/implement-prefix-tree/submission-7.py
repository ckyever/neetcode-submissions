class Node:
    def __init__(self, char: str = None):
        self.char = char
        self.is_word = False
        self.next = {}

class PrefixTree:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.next:
                new_node = Node(char)
                current.next[char] = new_node
            current = current.next[char]
        
        current.is_word = True

    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            if char not in current.next:
                return False
            current = current.next[char]
        
        return current.is_word

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            if char not in current.next:
                return False
            current = current.next[char]
        
        return True