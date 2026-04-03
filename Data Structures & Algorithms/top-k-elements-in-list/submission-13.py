class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums

        # Count each frequency of nums sort count list from highest to lowest and return the first k nums

        # Loop thorugh nums
            # Store in hashmap each num as key where value is count

        # Sort hashmap dict(sorted(x.items(), key=lambda item: item[1], reverse=True))
        # Return first k keys

        dictionary = {}

        for n in nums:
            dictionary[n] = dictionary.get(n, 0) + 1

        mostFrequentNums = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True)).keys()
        print(mostFrequentNums)

        return list(mostFrequentNums)[:k]
        
        