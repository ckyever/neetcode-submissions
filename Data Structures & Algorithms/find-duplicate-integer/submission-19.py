class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        new_slow = 0
        while True:
            new_slow = nums[new_slow]
            slow = nums[slow]
            if slow == new_slow:
                return new_slow
