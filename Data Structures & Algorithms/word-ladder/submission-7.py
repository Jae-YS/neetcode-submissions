from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        pattern_map = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                pattern_map[pattern].append(word)

        graph = defaultdict(list)

        for words in pattern_map.values():
            for w1 in words:
                for w2 in words:
                    if w1 != w2:
                        graph[w1].append(w2)        
        print(graph)
        def bfs(start, endWord, graph):
            visited = set([start])
            queue = deque([(start, 1)])

            while queue:
                curr, depth = queue.popleft()

                if curr == endWord:
                    return depth

                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, depth + 1))
            
            return 0

        return bfs(beginWord, endWord, graph)