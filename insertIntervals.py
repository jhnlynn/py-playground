from typing import List
from sortedcontainers import SortedDict


def insert(ls: List[int]) -> None:
    res = SortedDict()
    for i in range(len(ls)):
        res[ls[i]] = i
    print(res)


if __name__ == '__main__':
    ls = [3, 5, 1, 4, 6, 1, 3, 4]
    insert(ls)

