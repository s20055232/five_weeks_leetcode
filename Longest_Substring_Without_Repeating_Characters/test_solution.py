def test_solution_1(solution):
    s = "abcabcbb"
    assert solution.lengthOfLongestSubstring2(s) == 3


def test_solution_2(solution):
    s = "bbbbb"
    assert solution.lengthOfLongestSubstring2(s) == 1


def test_solution_3(solution):
    s = "pwwkew"
    assert solution.lengthOfLongestSubstring2(s) == 3


def test_solution_4(solution):
    s = " "
    assert solution.lengthOfLongestSubstring2(s) == 1


def test_solution_5(solution):
    s = "dvdf"
    assert solution.lengthOfLongestSubstring2(s) == 3


def test_solution_6(solution):
    s = "au"
    assert solution.lengthOfLongestSubstring2(s) == 2
