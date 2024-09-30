class CustomStack:

    def __init__(self, maxSize: int):
        self.max_size = maxSize
        self.size = 0
        self.data = [0] * self.max_size

    def push(self, x: int) -> None:
        if self._isFull():
            return
        self.data[self.size] = x
        self.size += 1

    def pop(self) -> int:
        if self._isEmpty():
            return -1
        self.size -= 1
        return self.data[self.size]

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, self.size)):
            self.data[i] += val

    def _isEmpty(self):
        return self.size == 0

    def _isFull(self):
        return self.size == self.max_size


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)