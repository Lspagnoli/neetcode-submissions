class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
    
        stack = []

        for t in tokens:

            if t == "+":
                    l = stack.pop()
                    r = stack.pop()
                    stack.append(r + l)
            elif t == "-":
                    l = stack.pop()
                    r = stack.pop()
                    stack.append(r - l)
            elif t == "*":
                    l = stack.pop()
                    r = stack.pop()
                    stack.append(l * r)
            elif t == "/":
                    l = stack.pop()
                    r = stack.pop()
                    stack.append(int(r / l))
            else:
                stack.append(int(t))
        
        return stack[0]