class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        for i, _ in enumerate(nums):
            product = 1
            for j, n in enumerate(nums):
                if i == j:
                    continue
                product *= n
            answer.append(product)

        return answer