class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # Initialise both hashmaps for all lowercase letters so we can use equality operator
        a_unicode, z_unicode = ord('a'), ord('z')
        s1_map, window = {}, {}
        for i in range(a_unicode, z_unicode + 1):
            s1_map[chr(i)] = 0
            window[chr(i)] = 0

        for char in s1:
            s1_map[char] += 1
        
        for char in s2[:len(s1)]:
            window[char] += 1

        left, right = 0, len(s1) - 1
        while right < len(s2):
            if s1_map == window:
                return True

            window[s2[left]] -= 1
            left += 1

            if right >= len(s2) - 1:
                break

            right += 1
            window[s2[right]] += 1

        return False 
