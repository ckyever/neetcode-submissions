class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        adj = defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for char in range(len(word)):
                pattern = word[:char] + "*" + word[char+1:]
                adj[pattern].append(word)

        visit = set([beginWord])
        queue = deque([beginWord])
        result = 1
        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return result

                for char in range(len(word)):
                    pattern = word[:char] + "*" + word[char+1:]
                    for neighbour in adj[pattern]:
                        if neighbour not in visit:
                            visit.add(neighbour)
                            queue.append(neighbour)
            result += 1

        return 0