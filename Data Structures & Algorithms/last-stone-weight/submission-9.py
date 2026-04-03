class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            stone1 = -heapq.heappop(stones)
            stone2 = -heapq.heappop(stones)

            if stone1 == stone2:
                # both destroyed so do nothing
                continue
            else:
                new_weight = abs(stone1 - stone2)
                heapq.heappush(stones, -new_weight)
        
        if stones:
            return -stones[0]
        else:
            return 0