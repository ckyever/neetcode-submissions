class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.max_heap = []

        for n in nums:
            i = 0
            while i < len(self.max_heap) and n < self.max_heap[i]:
                i += 1
            self.max_heap.insert(i, n)

    def add(self, val: int) -> int:
        i = 0
        while i < len(self.max_heap) and val < self.max_heap[i]:
            i += 1
        self.max_heap.insert(i, val)
        
        return self.max_heap[self.k-1]
        
