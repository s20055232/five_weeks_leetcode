def test_solution_1(solution):
    assert solution.containsDuplicate([1,2,3,1])

def test_solution_2(solution):
    assert solution.containsDuplicate([1,2,3,4]) is False

def test_solution_3(solution):
    assert solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2])

def test_solution2_1(solution):
    assert solution.containsDuplicate([1,2,3,1])

def test_solution2_2(solution):
    assert solution.containsDuplicate([1,2,3,4]) is False

def test_solution2_3(solution):
    assert solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2])