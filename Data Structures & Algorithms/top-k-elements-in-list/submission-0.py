from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create dict of nums where key is the number and value is the count
        #loop through each dict item and find the most freq number and add to list
        #decrement k after finding it
        #continue until k is 0

        # O(n) where n is the length of nums
        numsCount = defaultdict(int)
        for number in nums:
            numsCount[number] += 1

        output = []

        # O(m^2) where m is the number of unique integers in nums
        while k > 0:
            largestCount = 0
            mostFrequentNumber = None
            for number in numsCount.keys():
                if numsCount[number] > largestCount:
                    largestCount = numsCount[number]
                    mostFrequentNumber = number
            
            numsCount.pop(mostFrequentNumber)
            output.append(mostFrequentNumber)
            k -= 1
        
        return output
        
        