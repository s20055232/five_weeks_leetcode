def test_solution_1(solution):
    assert solution.twoSum([3, 3], 6) == [0, 1]


def test_solution_2(solution):
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]


def test_solution_3(solution):
    assert solution.twoSum([3, 2, 4], 6) == [1, 2]
