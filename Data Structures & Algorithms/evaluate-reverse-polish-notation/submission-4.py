class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = "+-/*"
        for idx, c in enumerate(tokens):
            if c not in operators:
                v = int(c)
                stack.append(v)
            else:
                if c == "+":
                    fv = stack.pop()
                    lv = stack.pop()
                    stack.append(lv+fv)
                elif c == "-":
                    fv = stack.pop()
                    lv = stack.pop()
                    stack.append(lv-fv)
                elif c == "/":
                    fv = stack.pop()
                    lv = stack.pop()
                    stack.append(int(lv/fv))
                elif c == "*":
                    fv = stack.pop()
                    lv = stack.pop()
                    stack.append(lv*fv)
        
        
        return stack[0]