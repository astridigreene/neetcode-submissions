class MinStack:

    def __init__(self):
        self.stack = []
        self.min_num = float('inf')

    def push(self, val: int) -> None:
        if val < self.min_num: self.min_num = val
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.min_num:
            self.stack.pop()
            self.min_num = float('inf')
            for i, num in enumerate(self.stack):
                if num < self.min_num: self.min_num = num
        else: self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_num
