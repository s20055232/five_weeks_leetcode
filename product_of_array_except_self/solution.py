class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = []
        for idx in range(len(nums)):
            total = 1
            for idx2, num in enumerate(nums):
                if idx == idx2:
                    continue
                else:
                    total *= num
            result.append(total)
        return result

    def productExceptSelf2(self, nums: list[int]) -> list[int]:
        length_of_nums = len(nums)
        result = [1] * length_of_nums

        prefix = 1
        for i in range(length_of_nums):
            result[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(length_of_nums - 1, -1, -1):
            result[i] = result[i] * suffix
            suffix *= nums[i]
        return result
