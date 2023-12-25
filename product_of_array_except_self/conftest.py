from solution import Solution
import pytest


@pytest.fixture(scope="module")
def solution():
    return Solution()
