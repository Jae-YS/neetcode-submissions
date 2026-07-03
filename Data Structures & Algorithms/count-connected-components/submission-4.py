from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjc = defaultdict(list)
        for x, y in edges:
            adjc[x].append(y)
            adjc[y].append(x) 

        visited = set()
        components = 0

        def dfs(node):
            for neigh in adjc[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    dfs(neigh)

        for i in range(n):
            if i not in visited:
                components += 1
                visited.add(i)
                dfs(i)
        
        return components
