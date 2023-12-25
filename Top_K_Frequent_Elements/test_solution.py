def test_solution_1(solution):
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    assert solution.topKFrequent(nums, k) == [1, 2]


def test_solution_2(solution):
    nums = [1]
    k = 1
    assert solution.topKFrequent(nums, k) == [1]
