class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = []
        for car, spe in zip(position, speed):
            fleet.append((car, spe))
        
        fleet.sort(key=lambda x: x[0])
        count = 0
        slowest = float('-inf')
        
        while fleet:
            cur_pos, cur_spe = fleet.pop()            
            itr = (target - cur_pos) / cur_spe 
            if itr <= slowest:
                continue      
            slowest = itr
            count += 1

        return count