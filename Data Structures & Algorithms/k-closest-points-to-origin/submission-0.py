class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p in points:
            ed = math.sqrt((p[0] - 0)**2 + (p[1] - 0)**2)
            heap.append((ed, p))
        heapq.heapify(heap)

        return [point for ed, point in heapq.nsmallest(k, heap)]