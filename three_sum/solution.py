class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        memo = []
        nums = sorted(nums)
        for pt in range(len(nums)):
            pointer = pt + 1
            result = self.twoSum(nums[pointer:], 0 - nums[pt])
            if result:
                print(pointer)
                [first, second] = result
                print(first)
                print(second)
                memo.append([nums[pt], nums[first + pointer], nums[second + pointer]])
        return memo


a = sorted([-1, 0, 1, 2, -1, -4])
Solution().threeSum(a)
