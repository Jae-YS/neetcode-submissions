class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = target
        px, py, pz = 0, 0, 0
        for i in range(len(triplets)):
            cx, cy, cz = triplets[i]
            if cx > x or cy > y or cz > z:
                continue 
            px = max(px, cx)
            py = max(py, cy)
            pz = max(pz, cz)
        


    
        return [px, py, pz] == target