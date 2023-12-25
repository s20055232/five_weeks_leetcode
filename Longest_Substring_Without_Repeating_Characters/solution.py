class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        for idx, char in enumerate(s):
            length = 1
            seen = set(char)
            if idx + 1 <= len(s) - 1:
                for slice_char in s[idx + 1 :]:
                    if slice_char in seen:
                        result = max(result, length)
                        break
                    else:
                        length += 1
                        seen.add(slice_char)
            result = max(result, length)

        return result

    def lengthOfLongestSubstring2(self, s: str) -> int:
        left_idx = 0
        seen = set()
        result = 0
        for right_idx, _ in enumerate(s):
            while s[right_idx] in seen:
                seen.remove(s[left_idx])
                left_idx += 1
            seen.add(s[right_idx])
            result = max(result, right_idx - left_idx + 1)

        return result
