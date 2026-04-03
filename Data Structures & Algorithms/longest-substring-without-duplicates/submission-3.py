class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)

        left, right = 0, 1
        substring = [s[left]]
        longest_substring = 0

        while right < len(s):
            if s[right] in substring:
                substring.remove(s[left])
                left += 1
            else:
                substring.append(s[right])
                longest_substring = max(longest_substring, len(substring))
                right += 1
            
        return longest_substring