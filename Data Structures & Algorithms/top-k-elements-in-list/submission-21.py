class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Loop thorugh nums
            # Store count in hashmap
        
        # Loop through hashmap add key into array of lists with length len(nums)
        # Loop through array in reverse index order
            # Loop through each list found
                # Add each value to result array and minus k
                # If k is 0 return the result array

        hashmap = {}
        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1
        print(hashmap)

        numsLength = len(nums)
        countList = [[] for _ in range(numsLength)]
        for key, value in hashmap.items():
            countList[value-1].append(key)
            print(countList)

        topKFrequent = []
        for i in range(numsLength-1, -1, -1):
            for num in countList[i]:
                topKFrequent.append(num)
                k -= 1
                if k == 0:
                    return topKFrequent

        raise Error("Inputs are invalid")
        
        