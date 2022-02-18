from collections import deque
from functools import lru_cache
from queue import PriorityQueue

from sortedcontainers import SortedDict, SortedList


class WordDictionary:

    # def __init__(self):
    #     self.root = {}
    #
    # def addWord(self, word: str) -> None:
    #     node = self.root
    #     for char in word:
    #         node = node.setdefault(char, {})
    #     node[None] = None
    #
    # def search(self, word: str) -> bool:
    #     def find(word: str, node: dict):
    #         if not word:
    #             return None in node
    #         char, word = word[0], word[1:]
    #         if char != '.':
    #             return char in node and find(word, node[char])
    #         return any(find(word, kid) for kid in node.values() if kid)
    #     print(find(word, self.root))
    #     return find(word, self.root)

    def __init__(self):
        self.root = {}

    @lru_cache
    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
        node[None] = None

    def search(self, word: str) -> bool:
        def find_trie(Word: str, node: dict) -> bool:
            if not Word:
                return None in node
            char, new_word = Word[0], Word[1:]
            if char != '.':
                return char in node and find_trie(new_word, node[char])
            for kid in node.values():
                if kid:
                    return find_trie(new_word, kid)

        return find_trie(word, self.root)


if __name__ == '__main__':
    # w = WordDictionary()
    # w.addWord('bad')
    # w.search("pad")
    # w.search("bad")
    # w.search("b..")
    #
    # s = deque()
    # s.append(1)
    # s.append(3)
    # s.append(-1)
    # s.append(-3)
    # s.append(5)

    # pq = PriorityQueue()
    # pq.put(1)
    # print(pq.qsize())

    # ss = [2, 4, 5, 1, 1]
    # res = [1, 3, 4, 5, 6, 6]
    # ss = res[:len(ss)]
    # print(ss)

    sd, sl = SortedDict(), SortedList()
    sd[1] = 1
    sd[2] = 3
    sd[8] = 21

    print(sd.popitem(0))
    
    sl.append((1, 0))
    sl.append((0, 3))
    print(sl)

    sbb = 'a'
    sss = 'b'

