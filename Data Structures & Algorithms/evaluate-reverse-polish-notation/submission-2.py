class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ["+","-","*","/"]:
                stack.append(token)
            else:
                a = stack.pop()
                b = stack.pop()
                if token == "+":
                    stack.append(int(a)+int(b))
                elif token ==  "-":
                    stack.append(int(b)-int(a))
                elif token == '*':
                    stack.append(int(a)*int(b))
                else: 
                    stack.append(int(b)/int(a))
        return int(stack[-1])
        