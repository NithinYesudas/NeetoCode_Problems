class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for operation in operations:
            if operation =="+":
                stack.append(stack[-1]+stack[-2])
            elif operation == "D":
                a = stack[-1]
                stack.append(2*a)
            elif operation == "C":
                stack.pop()
            else:
                stack.append(int(operation))
        return sum(stack)
        