def test_solution_1(solution):
    nums = [1, 2, 3, 4]
    assert solution.productExceptSelf(nums) == [24, 12, 8, 6]


def test_solution_2(solution):
    nums = [-1, 1, 0, -3, 3]
    assert solution.productExceptSelf(nums) == [0, 0, 9, 0, 0]


def test_solution2_1(solution):
    nums = [1, 2, 3, 4]
    assert solution.productExceptSelf2(nums) == [24, 12, 8, 6]


def test_solution2_2(solution):
    nums = [-1, 1, 0, -3, 3]
    assert solution.productExceptSelf2(nums) == [0, 0, 9, 0, 0]
