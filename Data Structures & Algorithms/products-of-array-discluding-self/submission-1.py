class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        count_of_zeroes = 0
        for number in nums:
            if number == 0:
                count_of_zeroes += 1
            else:
                total_product *= number
        result = []
        
        if count_of_zeroes > 1:
            result = [0 for _ in nums]
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
