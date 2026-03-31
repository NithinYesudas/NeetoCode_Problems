class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s)%2!=0:
            return False
        for bracket in s:
            if bracket in ['(' , '{' , '[']:
                stack.append(bracket)
                continue
            if len(stack):

                a = stack.pop()
            else:
                return False
            if bracket == ')' and a !='(':
                return False
            elif bracket == ']' and a != '[':
                return False
            elif bracket == '}' and a!= '{':
                return False
        if not len(stack):
            return True
        else:
            return False


        