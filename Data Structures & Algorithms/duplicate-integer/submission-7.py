class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = set()

        for number in nums:
            if number in hashmap:
                return True
            else:
                hashmap.add(number)
        
        return False