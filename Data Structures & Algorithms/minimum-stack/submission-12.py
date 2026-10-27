class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            low, _ = self.stack[-1]
            self.stack.append((min(low, val), val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        _, val = self.stack[-1]
        return val

    def getMin(self) -> int:
        low, _ = self.stack[-1]
        return low
