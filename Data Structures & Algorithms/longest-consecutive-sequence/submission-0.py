class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Convert list into hashmap
        numsHash = {}
        for number in nums:
            numsHash[number] = number

        # For each number in nums find it's longest sequence starting from that number
        longestSequence = 0
        for number in numsHash.keys():
            nextNumber = number + 1
            currentSequence = 1

            # As long as the next number in the sequence exists in the hashmap, keep looking
            while nextNumber in numsHash.keys():
                currentSequence += 1
                nextNumber += 1

            # We have reached the end of the sequence, check if it is the longest one
            if currentSequence > longestSequence:
                longestSequence = currentSequence

        return longestSequence