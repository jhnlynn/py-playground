def wordCompression(word: str, k: int) -> str:
    stack = []
    for c in word:
        if len(stack) == 0:
            stack.append([c, 1])
            continue

        top = stack[-1]
        if top[0] == c:
            if top[1] == k - 1:
                times = k - 1
                while times > 1:
                    times -= 1
                    stack.pop()
            else:
                stack.append([c, top[1] + 1])
        else:
            stack.append([c, 1])

    stack.reverse()
    res = ""
    for s in stack:
        res += s[0]

    return res


if __name__ == '__main__':
    word = "abbcccbb"
    k = 3

    print(wordCompression(word, k))
