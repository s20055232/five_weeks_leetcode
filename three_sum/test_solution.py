def test_solution_1(solution):
    nums = [-1, 0, 1, 2, -1, -4]
    assert solution.threeSum(nums) == [[-1, -1, 2], [-1, 0, 1]]


def test_solution_2(solution):
    nums = [0, 1, 1]
    assert solution.threeSum(nums) == []


def test_solution3(solution):
    nums = [0, 0, 0]
    assert solution.threeSum(nums) == [[0, 0, 0]]


def test_solution4(solution):
    nums = [-1, 0, 1, 0]
    assert solution.threeSum(nums) == [[-1, 0, 1]]
