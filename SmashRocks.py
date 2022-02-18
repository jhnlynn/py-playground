import heapq
from typing import List


class SmashIt:
    def SmashRocks(self, A: List[int]) -> int:
        for i in range(len(A)):
            A[i] *= (-1)

        heapq.heapify(A)  # pq

        while len(A) > 0:
            a, b = heapq.heappop(A), 0
            if len(A) > 0:
                b = heapq.heappop(A)
            if b == 0:
                return -a

            c = abs(a - b)
            if c != 0:
                heapq.heappush(A, -c)

        if len(A) > 0:
            return A.pop()*(-1)
        else:
            return 0


if __name__ == '__main__':
    s = SmashIt()

    print(s.SmashRocks([1, 1, 2, 3, 6, 7, 7]))
