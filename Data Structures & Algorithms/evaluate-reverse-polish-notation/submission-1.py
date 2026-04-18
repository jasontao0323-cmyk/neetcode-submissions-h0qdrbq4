# evalRPN
# Stack: Intuition V\Reverse Polish Notation (RPN) is well-suited 
# for stack evaluation because the most recent numbers are always used next. 
# Numbers are pushed onto the stack, and operators pop the top two numbers, 
# apply the operation, and push the result back. 
# TC: O(n)
# SC: O(n)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(c))
        return stack[0]