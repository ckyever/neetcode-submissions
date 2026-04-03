class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # loop through each temperature
            # keep track of index and look for temperature after this one where it is greater
            # if found add index to the list
            # if we reach end of the list add 0 as the index

        #[30,38,30,36,35,40,28]

        result = []

        for i, temp in enumerate(temperatures):
            foundWarmerTemp = False
            for j, nextTemp in enumerate(temperatures[i+1:]):
                if nextTemp > temp:
                    result.append(j+1)
                    foundWarmerTemp = True
                    break
            if not foundWarmerTemp:
                result.append(0)

        return result