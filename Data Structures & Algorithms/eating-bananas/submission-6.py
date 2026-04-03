class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low_k, high_k = 1, max(piles)

        result = high_k

        while low_k <= high_k:
            mid_k = (low_k + high_k) // 2
            
            hours = 0
            for p in piles:
                hours += math.ceil(p / mid_k)
            
            if hours > h:
                low_k = mid_k + 1
            else:
                high_k = mid_k - 1
                result = mid_k
        
        return result
            
