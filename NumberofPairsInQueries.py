from typing import List


class NumberOfPairs:
    """
Given 3 arrays, A, B and queries. there are 2 forms of query. [0, i, j] means we need to update B[i] = j.
Another type is [1, k], which means we need to find out the number of pairs in in A and B that sums up to k (1 from A and another from B).
The number in a and b is guaranteed to be greater than or equal to 0.
For example:
a = [1,2,3]
b = [2,4]
query = [[1,5], [0, 0, 1], [1, 5]]
For the first query, [1, 5], we can find 2 pairs, (1,4) and (3,2)
For the second query, we update b[0] = 1, so now b = [1,4]
For the third query, we can only find one pair to sum up to 5, which is (1,4)


    """

    def numberOfPairs(self, arr1: List[int], arr2: List[int], query: List[List[int]]):

        def initialization():
            for i, n in enumerate(arr1):
                a_map[i] = n
            for i, n in enumerate(arr2):
                b_map[i] = n

        a_map, b_map = {}, {}
        initialization()

        for q in query:
            if q[0] == 0:  # update
                i, j = q[1], q[2]
                b_map[i] = j
                arr2[i] = j
                print(arr2)

            else:  # find pairs
                target, res = q[1], []
                for aa in a_map:
                    if (target - arr1[aa]) in b_map.values():
                        res.append(list([arr1[aa], target - arr1[aa]]))
                print(res)


if __name__ == '__main__':
    a, b, q = [1, 2, 3], [2, 4], [[1, 5], [0, 0, 1], [1, 5]]
    nop = NumberOfPairs()
    nop.numberOfPairs(a, b, q)
