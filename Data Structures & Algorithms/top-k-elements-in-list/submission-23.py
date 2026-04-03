class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1

        nums_length = len(nums)
        count_list = [[] for _ in range(nums_length)]
        for key, value in hashmap.items():
            count_list[value-1].append(key)

        top_k_frequent = []
        for i in range(nums_length-1, -1, -1):
            for num in count_list[i]:
                top_k_frequent.append(num)
                k -= 1
                if k == 0:
                    return top_k_frequent

        raise Error("Inputs are invalid")
        
        