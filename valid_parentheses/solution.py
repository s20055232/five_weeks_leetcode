class Solution:
    def isValid(self, s: str) -> bool:
        queue = []
        parentheses_pairs = {"(": ")", "{": "}", "[": "]"}

        for char in s:
            if char in parentheses_pairs:
                queue.append(char)
            else:
                if not queue or char != parentheses_pairs[queue.pop()]:
                    return False

        return len(queue) == 0
