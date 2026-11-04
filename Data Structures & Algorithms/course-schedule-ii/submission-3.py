class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        for a, b in prerequisites:
            graph.setdefault(b, []).append(a)
        
        state = [0] * numCourses
        retVal = []
        has_cycle = False

        def dfs(node):
            nonlocal has_cycle
            if has_cycle:
                return
            
            state[node] = 1
            for neighbor in graph.get(node, []):
                if state[neighbor] == 1:
                    has_cycle = True
                    return
                elif state[neighbor] == 0:
                    dfs(neighbor)
            state[node] = 2
            retVal.append(node)
        
        for i in range(numCourses):
            if state[i] == 0:
                dfs(i)
                if has_cycle:
                    return []
        
        return retVal[::-1]