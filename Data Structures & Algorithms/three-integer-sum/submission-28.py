class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:        
        answers = set()
        distinct_nums = {}

        for index, num in enumerate(nums):
            distinct_nums[num] = index

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                third_num = -1 * (nums[i] + nums[j])

                third_num_index = distinct_nums.get(third_num, None)

                if third_num_index and third_num_index != i and third_num_index != j:
                    answer = sorted([nums[i], nums[j], third_num])
                    key = ",".join(map(str, answer))
                    answers.add(key)

        output = []
        for triplet in answers:
            output.append(map(int, triplet.split(",")))

        return output


