class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.queue = [None] * self.capacity
        self.front = 0
        self.rear = 0
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.capacity == self.size:
            return False
        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -=1
        return True

    def Front(self) -> int:
        if self.size == 0:
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        return self.queue[(self.rear - 1) % self.capacity]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()