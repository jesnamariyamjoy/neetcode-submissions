from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair position and speed, then sort by position in descending order
        cars = sorted(zip(position, speed), reverse=True)
        
        stack = []
        for pos, spd in cars:
            # Calculate time to reach the target
            time = (target - pos) / spd
            
            # If stack is not empty and the current car arrives faster than or 
            # at the same time as the car/fleet ahead of it, it merges into that fleet.
            if stack and time <= stack[-1]:
                continue
            
            # Otherwise, it forms a new fleet
            stack.append(time)
            
        return len(stack)