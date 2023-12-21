class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        mapping = {}
        result = []
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in mapping:
                return [mapping[diff], idx]
            mapping[num] = idx
        return result