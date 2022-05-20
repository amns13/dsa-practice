MINIMUM_SIZE = 5

class Queue:
    def __init__(self, size=MINIMUM_SIZE):
        self.size: int = size
        self.front: int= size
        self.back: int = 0
        self.data: list[int] = [0] * (size + 1)

    def empty(self) -> bool:
        return (self.front + 1) % (self.size + 1) == self.back

    def full(self) -> bool:
        return self.front == self.back

    def enqueue(self, value: int) -> None:
        if self.full():
            raise OverflowError("Queue is full")
        
        self.data[self.back] = value
        self.back = (self.back + 1) % (self.size + 1)
        
    def dequeue(self) -> int:
        if self.empty():
            raise IndexError("Queue is empty")

        self.front = (self.front + 1) % (self.size + 1)
        return self.data[self.front]
        