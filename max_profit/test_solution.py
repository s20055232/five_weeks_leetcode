def test_solution_1(solution):
    assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 5


def test_solution_2(solution):
    assert solution.maxProfit([7, 6, 4, 3, 1]) == 0


def test_solution2_1(solution):
    assert solution.maxProfit2([7, 1, 5, 3, 6, 4]) == 5


def test_solution2_2(solution):
    assert solution.maxProfit2([7, 6, 4, 3, 1]) == 0
