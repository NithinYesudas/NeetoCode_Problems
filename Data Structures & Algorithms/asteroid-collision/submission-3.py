class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while len(stack) and stack[-1]>0 and asteroid<0:
                top = stack.pop()
                if abs(top) == abs(asteroid):
                    asteroid = None
                    break
                else:
                    asteroid = top if max(abs(top),abs(asteroid)) == abs(top) else asteroid
            if asteroid:
                stack.append(asteroid)
        return stack
                
        