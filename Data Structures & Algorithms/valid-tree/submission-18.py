class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        seen = set()    
        edges.sort()
        seen.add(0)
        for x, y in edges:
            if x in seen or y in seen:
                seen.add(x)
                seen.add(y)
        
        print(seen)


        return len(seen) == n