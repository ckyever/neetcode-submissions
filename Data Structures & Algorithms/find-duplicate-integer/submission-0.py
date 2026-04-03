class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        chars = ""
        for n in nums:
            n_string = f",{n},"
            if n_string in chars:
                return n
            else:
                chars += n_string
        
        raise Error("Invalid input")