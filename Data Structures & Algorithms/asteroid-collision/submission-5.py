class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for curr in asteroids:
            alive = True
          
            while alive and stack and stack[-1] > 0 and curr < 0:
                top = stack[-1]
                if top < -curr:
 
                    stack.pop()
 
                elif top == -curr:
 
                    stack.pop()
                    alive = False
                else:
                    
                    alive = False
            if alive:
                stack.append(curr)
        return stack
