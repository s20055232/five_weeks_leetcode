def all_elements_same(source, target):
    sorted_source = sorted([sorted(i) for i in source])
    sorted_target = sorted([sorted(i) for i in target])
    for i in sorted_source:
        if i not in sorted_target:
            raise ValueError("element not equal")


def test_solution_1(solution):
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    assert (
        all_elements_same(
            solution.groupAnagrams(strs),
            [
                ["bat"],
                ["nat", "tan"],
                ["ate", "eat", "tea"],
            ],
        )
        is None
    )


def test_solution_2(solution):
    strs = [""]
    assert all_elements_same(solution.groupAnagrams(strs), [[""]]) is None


def test_solution_3(solution):
    strs = ["a"]
    assert all_elements_same(solution.groupAnagrams(strs), [["a"]]) is None


def test_solution2_1(solution):
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    assert (
        all_elements_same(
            solution.groupAnagrams2(strs),
            [
                ["bat"],
                ["nat", "tan"],
                ["ate", "eat", "tea"],
            ],
        )
        is None
    )


def test_solution2_2(solution):
    strs = [""]
    assert all_elements_same(solution.groupAnagrams2(strs), [[""]]) is None


def test_solution2_3(solution):
    strs = ["a"]
    assert all_elements_same(solution.groupAnagrams2(strs), [["a"]]) is None
