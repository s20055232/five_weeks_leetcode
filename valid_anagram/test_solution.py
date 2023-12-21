def test_solution_1(solution):
    assert solution.isAnagram("anagram", "nagaram")


def test_solution_2(solution):
    assert solution.isAnagram("rat", "car") is False


def test_solution2_1(solution):
    assert solution.isAnagram2("anagram", "nagaram")


def test_solution2_2(solution):
    assert solution.isAnagram2("rat", "car") is False


def test_solution3_1(solution):
    assert solution.isAnagram3("anagram", "nagaram")


def test_solution3_2(solution):
    assert solution.isAnagram3("rat", "car") is False
