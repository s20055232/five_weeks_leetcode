class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums = sorted(nums)

        for idx, val in enumerate(nums):
            if idx > 0 and nums[idx - 1] == val:
                continue

            left, right = idx + 1, len(nums) - 1
            while left < right:
                total = val + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([val, nums[left], nums[right]])
                    left += 1
                    # add number until not repeat
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return result
