import bisect
import collections
import math
from typing import List


def nearestCity(Points: List[str], XCoordinates: List[int], YCoordinates: List[int]
                , QueriedPoints: List[str]) -> List[str]:
    XY, sameXY = {}, [collections.defaultdict(dict), collections.defaultdict(dict)]
    for p, x, y in zip(Points, XCoordinates, YCoordinates):
        XY[p] = (x, y), (y, x)
        for (x, y), same in zip(XY[p], sameXY):
            same[x][y] = p
    sortXY = [{x: sorted(y) for x, y in same.items()} for same in sameXY]

    Near = collections.namedtuple("Near", ["distance", "point"])
    none, res = Near(math.inf, ""), []
    for p in QueriedPoints:
        near = none
        for (x, y), same, sort in zip(XY[p], sameXY, sortXY):
            i = bisect.bisect_left(sort[x], y)
            near = min(
                near,
                Near(y - sort[x][i - 1], same[x][sort[x][i - 1]]) if i else none,
                Near(sort[x][i + 1] - y, same[x][sort[x][i + 1]]) if i < len(sort[x]) - 1 else none,
            )
        res.append(near.point)
    return res


if __name__ == '__main__':
    # numOfPoints = 3
    #
    # points = ["p1", "p2", "p3"]
    #
    # xCoordinates = [30, 20, 10]
    #
    # yCoordinates = [30, 20, 30]
    #
    # numOfQueriedPoints = 3
    #
    # queriedPoints = ["p3", "p2", "p1"]

    numOfPoints = 5

    points = ["p1", "p2", "p3", "p4", "p5"]

    xCoordinates = [10, 20, 30, 40, 50]

    yCoordinates = [10, 20, 30, 40, 50]

    numOfQueriedPoints = 5

    queriedPoints = ["p1", "p2", "p3", "p4", "p5"]

    print(nearestCity(points, xCoordinates, yCoordinates, queriedPoints))
