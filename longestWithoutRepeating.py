def lengthOfLongestSubstring(self, A: str) -> int:
    """

    """
    max_len, i, j, dic = 0, 0, 0, {}

    for j in range(len(A)):
        if A[j] in dic:
            i = max(i, dic[A[j]] + 1)

        dic[A[j]] = j
        max_len = max(max_len, j - i + 1)

    return max_len
