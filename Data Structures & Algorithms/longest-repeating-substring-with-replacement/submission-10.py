class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        longest_substring = 0
        left = 0

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)

            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1

            longest_substring = max(longest_substring, right - left + 1)
        
        return longest_substring

                