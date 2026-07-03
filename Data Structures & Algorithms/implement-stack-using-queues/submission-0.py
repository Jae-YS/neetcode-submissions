from collections import deque

class MyStack:

    def __init__(self):
        self.queue = deque() 

    def push(self, x: int) -> None:
        self.queue.append(x)
        return

    def pop(self) -> int:
        temp = deque()
        while len(self.queue):
            last = self.queue.popleft()
            if len(self.queue):
                temp.append(last)
        self.queue = temp
        return last

    def top(self) -> int:
        temp = deque()
        while len(self.queue):
            last = self.queue.popleft()
            temp.append(last)
        self.queue = temp
        return last

    def empty(self) -> bool:
        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()