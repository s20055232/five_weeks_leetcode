def test_solution_1(solution):
    s = "()"
    assert solution.isValid(s)


def test_solution_2(solution):
    s = "()[]{}"
    assert solution.isValid(s)


def test_solution_3(solution):
    s = "(]"
    assert not solution.isValid(s)


def test_solution_4(solution):
    s = "["
    assert not solution.isValid(s)


def test_solution_5(solution):
    s = "]"
    assert not solution.isValid(s)
