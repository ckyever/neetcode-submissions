class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_hashmap = {}
        t_hashmap = {}
        for i in range(len(s)):
            if s[i] in s_hashmap:
                s_hashmap[s[i]] += 1
            else:
                s_hashmap[s[i]] = 1

            if t[i] in t_hashmap:
                t_hashmap[t[i]] += 1
            else:
                t_hashmap[t[i]] = 1

        return s_hashmap == t_hashmap