class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        result = []
        record = {}
        for num in nums:
            if num not in record:
                record[num] = 1
            else:
                record[num] += 1

        def _sort_helper(x):
            return x[1]

        result = sorted(record.items(), key=_sort_helper, reverse=True)

        result = [result.pop(0)[0] for _ in range(k)]
        return result
