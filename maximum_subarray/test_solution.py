def test_solution_1(solution):
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert solution.maxSubArray(nums) == 6


def test_solution_2(solution):
    nums = [1]
    assert solution.maxSubArray(nums) == 1


def test_solution_3(solution):
    nums = [5, 4, -1, 7, 8]
    assert solution.maxSubArray(nums) == 23
