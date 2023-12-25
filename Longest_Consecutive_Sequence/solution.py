class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # Time Limit
        from_to = {}
        for num in nums:
            if num - 1 in from_to:
                from_to[num - 1] = num
            if num + 1 in from_to:
                from_to[num] = num + 1
            if num not in from_to:
                from_to[num] = None

        all_result = [0]
        for num in from_to:
            result = 1
            while from_to[num] is not None:
                num = from_to[num]
                result += 1
            all_result.append(result)
        return max(all_result)

    def longestConsecutive2(self, nums: list[int]) -> int:
        result, current_streak = 0, 0
        num_set = set(nums)
        for num in num_set:
            if num - 1 not in num_set:
                current = num
                current_streak = 1
                while current + 1 in num_set:
                    current += 1
                    current_streak += 1

            result = max(result, current_streak)
        return result
