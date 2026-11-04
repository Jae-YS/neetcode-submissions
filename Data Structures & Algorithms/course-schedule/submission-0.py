class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for a, b in prerequisites:
            graph.setdefault(b, []).append(a)
        

        visited = {node: 0 for node in graph}

        def dfs(node):
            if visited.get(node, 0) == 1:
                return True
            if visited.get(node, 0) == 2:
                return False
            visited[node] = 1

            for neighbor in graph.get(node, []):
                if dfs(neighbor):
                    return True
            visited[node] = 2
            return False
        

        for node in graph:
            if visited[node] == 0:
                if dfs(node):
                    return False
        
        return True