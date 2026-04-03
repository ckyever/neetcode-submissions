class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        [-1,0,1,2,3]

        total_product = 1
        count_of_zeroes = 0
        for number in nums:
            if number == 0:
                count_of_zeroes += 1
            else:
                total_product *= number
        result = []
        
        # If more than one 0 exists then all answers will be 0
        if count_of_zeroes > 1:
            result = [0 for _ in nums]
        # If exactly one 0 exists then all answers except for the 0 index will be 0
        elif count_of_zeroes == 1:
            for number in nums:
                if number == 0:
                    result.append(int(total_product))
                else:
                    result.append(0)
        else:
            for number in nums:
                result.append(int(total_product/number))

        return result
