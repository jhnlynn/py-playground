# https://leetcode.com/discuss/interview-question/910599/robinhood-oa
from collections import deque


class OutOfLabyrinth:

    def traverse(self, row, col, obstacle, teleports):
        # row * col
        lab = [[0 for _ in range(row)] for _ in range(col)]

        # mark obstacles
        for obs in obstacle:
            x, y = obs
            lab[x][y] = -1

        # mark teleports
        teleMap = {}
        for tele in teleports:
            x, y, r, c = tele
            teleMap[(x, y)] = (r, c)
            lab[x][y] = -2  # mark start as -2

        q = deque()
        q.append((0, 0))
        step = 1

        while q:
            size = len(q)
            step += 1
            for i in range(size):
                r, c = q.popleft()
                if r == row - 1 and c == col - 1:
                    return step

                # we cannot step on an obstacle or out of border
                # so process the current position, then check next steps

                # if teleport
                if lab[r][c] == -2:
                    # check if it's infinite tele
                    x, y = teleMap[(r, c)]
                    if lab[x][y] == -1:  # visited
                        # or if x < r or y < c,
                        # because we only go down or go right
                        return -2
                    q.append((x, y))

                # mark the current position as visited
                lab[r][c] = -1

                if c + 1 >= col:  # next is right border
                    # now it cannot be: r + 1 >= row, because we have check it above
                    if lab[r + 1][c] == -2:  # teleport
                        q.append((r + 1, c))
                        break
                    if lab[r + 1][c] == -1:  # right out of border, and down is an obstacle
                        return -1

                # right step is obstacle,
                # and down step is out of border, or is also obstacle
                if lab[r][c + 1] == -1:
                    if r + 1 >= row or lab[r + 1][c] == -1:
                        # down and right are both obstacles
                        return -1
                    q.append((r + 1, c))

        return step


if __name__ == '__main__':
    # obs, teleport
    group = [
        (3, 3, [[2, 1]], [[0, 1, 2, 0]]),
        (3, 4, [[1, 1, ]], [[0, 2, 0, 1], [0, 3, 2, 0]]),
        (3, 4, [[2, 0], [1, 0]], [[0, 1, 1, 1], [1, 2, 0, 2], [0, 3, 2, 1]])
    ]

    ool = OutOfLabyrinth()
    i = 0
    n, m, obs, tele = group[i]
    print(ool.traverse(n, m, obs, tele))
