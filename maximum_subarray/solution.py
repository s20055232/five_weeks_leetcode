class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        tmp = [nums[0]]

        for idx in range(1, len(nums)):
            # 如果加入前面有比較好，就加入前面
            if nums[idx] + tmp[idx - 1] > nums[idx]:
                tmp.append(nums[idx] + tmp[idx - 1])
            else:  # 不然就從自己開始往後看
                tmp.append(nums[idx])
        return max(tmp)


# def maxSubarray(nums: list[int]) -> int:
#     if len(nums) == 0:
#         raise ValueError("wrong input")
#     result = [nums[0]]
#     for idx in range(1, len(nums)):
#         join_prev_group = result[idx - 1] + nums[idx]
#         current = nums[idx]
#         if join_prev_group > current:
#             result.append(join_prev_group)
#         else:
#             result.append(current)

#     return max(result)
