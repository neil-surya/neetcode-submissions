class MinStack:

    def __init__(self):
        self.stack: list[int] = []
        self.minimum: list[int] = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minimum or val <= self.minimum[-1]:
            self.minimum.append(val)

    def pop(self) -> None:
        if self.stack.pop() == self.minimum[-1]:
            self.minimum.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def getMin(self) -> int:
        return self.minimum[-1]