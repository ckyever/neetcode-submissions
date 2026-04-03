class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = [None] * capacity


    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        for index, value in enumerate(self.array):
            if value is None:
                self.array[index] = n
                return
        newIndex = self.getCapacity()
        self.resize()
        self.array[newIndex] = n


    def popback(self) -> int:
        for index in range(self.capacity-1, -1, -1):
            if self.array[index] != None:
                print(f"array[{index}] = {self.array[index]}")
                poppedValue = self.array[index]
                self.array[index] = None
                return poppedValue
        raise RuntimeError("Array is empty")

    def resize(self) -> None:
        currentSize = self.getCapacity()
        extraCapacity = [None] * currentSize
        self.array += extraCapacity
        self.capacity *= 2

    def getSize(self) -> int:
        size = 0
        for x in self.array:
            if x != None: 
                size += 1
        return size
    
    def getCapacity(self) -> int:
        return self.capacity

