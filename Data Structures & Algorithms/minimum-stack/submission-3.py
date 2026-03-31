class MinStack:

    def __init__(self):
        self.min_list = []
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not len(self.min_list) or self.min_list[-1]>=val:
            self.min_list.append(val)
        

    def pop(self) -> None:
        a = self.stack.pop()
        if a == self.min_list[-1]:
            self.min_list.pop()
        return a
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_list[-1]
        
