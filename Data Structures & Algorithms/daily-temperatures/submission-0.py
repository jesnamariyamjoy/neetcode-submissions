from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []  # Stores indices of temperatures
        
        for i, temp in enumerate(temperatures):
            # Pop elements from the stack while the current temperature is warmer
            # than the temperature at the index on top of the stack
            while stack and temperatures[stack[-1]] < temp:
                prev_index = stack.pop()
                res[prev_index] = i - prev_index
            
            # Push the current index onto the stack
            stack.append(i)
            
        return res