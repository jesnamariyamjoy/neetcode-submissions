from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            elif token == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif token == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            elif token == "/":
                b = stack.pop()
                a = stack.pop()
                # int() truncates toward zero (e.g., -3 / 2 = -1.5 -> -1)
                stack.append(int(a / b))
            else:
                stack.append(int(token))
                
        return stack[0]