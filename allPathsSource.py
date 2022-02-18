from queue import Queue
from typing import List


class allPathsSource:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
        1. have [(0, [0])]
        2. every element in graph[index]
        """
        q, res = Queue(), []
        target = len(graph) - 1
        q.put((0, [0]))

        while not q.empty():
            index, ls = q.get()
            if index == target:
                res.append(ls)
            else:
                for num in graph[index]:
                    q.put((num, ls + [num]))

        return res


if __name__ == '__main__':
    al = allPathsSource()
    print(al.allPathsSourceTarget([[1, 2], [3], [3], []]))
