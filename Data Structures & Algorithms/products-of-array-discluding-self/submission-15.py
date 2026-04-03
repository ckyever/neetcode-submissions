class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        answer = [None] * len(nums)
        answer[0] = 1
        for i in range(0, len(nums)-1):
            product *= nums[i]
            answer[i+1] = product
        print(answer)

        product = 1
        for i in range(len(nums)-1, 0, -1):
            product *= nums[i]
            print(product)
            answer[i-1] *= product

        return answer