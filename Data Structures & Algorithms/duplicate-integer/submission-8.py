class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for number in nums:
            if number in hashset:
                return True
            else:
                hashset.add(number)
        
        return False