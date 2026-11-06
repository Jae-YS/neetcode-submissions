class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        
        con = {}
        
        for x, y in edges:
            con.setdefault(x, []).append(y)
            con.setdefault(y, []).append(x)
        
        node = {i: 0 for i in range(n)}
        count = 0 
        
        def dfs(i):
            if node[i] == 1:
                return
            
            node[i] = 1
            for neighbor in con.get(i, []):
                if node[neighbor] != 1:
                    dfs(neighbor)
            
            return    

        for i in range(n):
            if node[i] != 1:
                dfs(i)
                count += 1

        return count