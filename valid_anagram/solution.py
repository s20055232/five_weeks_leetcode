class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        return sorted_s == sorted_t

    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = {}
        for char in s:
            counter.setdefault(char, 0)
            counter[char] += 1
        for char in t:
            if not counter.get(char):
                return False
            else:
                counter[char] -= 1
        return True

    def isAnagram3(self, s: str, t: str) -> bool:
        from collections import Counter

        return Counter(s) == Counter(t)
