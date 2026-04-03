class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsHash = set(nums)

        longestChain = 0
        for n in nums:
            if n-1 not in numsHash:
                print(n)
                # Start of a potential chain
                nextNumber = n + 1
                count = 1
                while nextNumber in numsHash:
                    nextNumber += 1
                    count += 1
                if count > longestChain:
                    longestChain = count

        return longestChain