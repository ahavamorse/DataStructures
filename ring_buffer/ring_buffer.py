class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.values = [None] * capacity
        self.nextIndex = 0

    def append(self, item):
        self.values[self.nextIndex] = item
        if self.nextIndex == self.capacity - 1:
            self.nextIndex = 0
        else:
            self.nextIndex += 1

    def get(self):
        returnArray = []
        for i in range(0, self.capacity):
            item = self.values[i]
            if item is not None:
                returnArray.append(item)
        return returnArray
