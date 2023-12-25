from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        sub_boxes = defaultdict(lambda: set())
        rows = defaultdict(lambda: set())
        columns = defaultdict(lambda: set())
        for x in range(len(board)):
            for y in range(len(board[x])):
                value = board[x][y]
                if value == ".":
                    continue

                if value in columns[x]:
                    return False
                else:
                    columns[x].add(value)

                if value in sub_boxes[(x // 3, y // 3)]:
                    return False
                else:
                    sub_boxes[(x // 3, y // 3)].add(value)

                if value in rows[y]:
                    return False
                else:
                    rows[y].add(value)
        return True
