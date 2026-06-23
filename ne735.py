#735. Asteroid Collision. We are given an array asteroids of integers representing asteroids in a row. The indices of the asteroid in the array represent their relative position in space. For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []

        for asteroid in asteroids:
            alive = True

            while alive and stack and stack[-1] > 0 and asteroid < 0:

                # current asteroid is bigger
                if abs(asteroid) > stack[-1]:
                    stack.pop()

                # both are equal
                elif abs(asteroid) == stack[-1]:
                    stack.pop()
                    alive = False

                # stack asteroid is bigger
                else:
                    alive = False

            if alive:
                stack.append(asteroid)

        return stack