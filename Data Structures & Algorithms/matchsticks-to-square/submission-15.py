from collections import defaultdict

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        sum_of_squares = sum(matchsticks)
        if sum_of_squares % 4 != 0:
            return False
        
        
        target = sum_of_squares // 4
        matchsticks.sort(reverse=True)
        
        sides = [0, 0, 0, 0]
        def dfs(i):
        
            if i == len(matchsticks):
                count = 0
                for side in sides:
                    if side == target:
                        count += 1 
                return count

            for j in range(4):
                if sides[j] + matchsticks[i] <= target:
                    sides[j] += matchsticks[i]

                    if dfs(i+1): return True
                    sides[j] -= matchsticks[i]
                
                if sides[j] == 0:
                    break

            return False

        return dfs(0)

        
