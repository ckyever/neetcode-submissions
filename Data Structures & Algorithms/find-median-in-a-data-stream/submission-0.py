class MedianFinder:

    def __init__(self):
        self.leftHeap = []
        self.rightHeap = []

    def addNum(self, num: int) -> None:
        if not self.leftHeap and not self.rightHeap:
            heapq.heappush(self.leftHeap, -num)
            return

        if -num > self.leftHeap[0]:
            heapq.heappush(self.leftHeap, -num)
        else:
            heapq.heappush(self.rightHeap, num)

        if len(self.leftHeap) > len(self.rightHeap) + 1:
            moveNum = heapq.heappop(self.leftHeap)
            heapq.heappush(self.rightHeap, -moveNum)

        if len(self.rightHeap) > len(self.leftHeap) + 1:
            moveNum = heapq.heappop(self.rightHeap)
            heapq.heappush(self.leftHeap, -moveNum)

    def findMedian(self) -> float:
        if len(self.leftHeap) == len(self.rightHeap):
            return (-self.leftHeap[0] + self.rightHeap[0]) / 2
        else:
            if len(self.leftHeap) > len(self.rightHeap):
                return -self.leftHeap[0]
            else:
                return self.rightHeap[0]
        
        