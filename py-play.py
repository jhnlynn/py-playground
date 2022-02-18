import heapq
from queue import LifoQueue
from typing import List


def sort_func(a, b):
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return a - b


def find_numbers(nums: List[int]) -> int:
    cnt = 0

    for num in nums:
        digits = 1
        while num // 10 != 0:
            digits += 1
            num = num // 10
        if digits % 2 == 0:
            cnt += 1

    return cnt


class Solution:
    pass


def get_it(it: int, that: int) -> (int, int):
    return it, that


def dfs(self, graph: [], s: int, d: int, visited: set()) -> bool:
    # if s has no edges out
    if graph[s] is None or s in visited:
        return False

    visited.add(s)
    # if found d in edges [d, s]
    if d in graph[s]:
        return True

    for elem in graph[s]:
        # if visited before, we remove
        graph[s].remove(elem)

        self.dfs(graph, elem, d, visited)

    return False


if __name__ == "__main__":
    s = [1, 7, 2, 4]
    # k = 3
    # st = set()
    #
    # for i in range(len(s)):
    #     for j in range(i + 1, len(s)):
    #         if (s[i] + s[j]) % k == 0:
    #             st.add(s[i])
    #             st.add(s[j])
    #
    # # print(len(st))
    # d = s.copy()
    # d.append(6)
    # print(s)
    # print(d)

    # i, j = get_it(1, 3)
    # print(i, j)

    # print(' '.join(f'{s}' for s in range(5)))
    q = LifoQueue()

    a = q.get()

    print(a)