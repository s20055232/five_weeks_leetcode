from collections import Counter


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = {}
        for str in strs:
            result.setdefault(frozenset(Counter(str).items()), []).append(str)

        return list(result.values())

    def groupAnagrams2(self, strs: list[str]) -> list[list[str]]:
        result = {}
        for str in strs:
            sorted_str = "".join(sorted(str))
            result.setdefault(sorted_str, []).append(str)

        return list(result.values())
