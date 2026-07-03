from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # adj list
        neighbor = defaultdict(list)

        for edge in edges:
            l, r = edge
            neighbor[l].append(r) 
            neighbor[r].append(l)
        
        visited = set()
        def dfs(curr, visited, parent):
            visited.add(curr)
            for node in neighbor[curr]:
                if node in visited and node != parent:
                    return False
                else:
                    if node == parent:
                        continue
                    val = dfs(node, visited, curr)
                    if val == False:
                        return False
                   
            return True
            
        val = dfs(0, visited, -1)    

        return val and n == len(visited)

        



