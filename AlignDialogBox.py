messages = [["1", "Hello how r u"], ["2", "good ty"],
            ["2", "u"], ["1", "me too bro"]]

width, user_width = 15, 5


def solve():
    res = []
    for message in messages:
        user, content = message
        arr = content.split(" ")
        temp = []
        curr_length = 0
        index = 0
        while index < len(arr):
            new_length = curr_length + len(arr[index])
            # spaces to separate words
            if curr_length != 0:
                new_length += 1
            if new_length <= user_width:
                curr_length = new_length
                temp.extend([" ", arr[index]])
                index += 1
            else:
                res.append([user, "".join(temp).strip()])
                curr_length = 0
                temp = []

        # after while, there can still be some words remaining in 'tmp'
        # we need to squeeze them out
        if temp:
            res.append([user, "".join(temp).strip()])

    for x in _generate_content(res, width):
        print(x)


def _generate_content(array, width):
    bar = '+' + ''.join(['*'] * width) + '+'
    res = []
    res.append(bar)
    for user, message in array:
        if user == '1':
            temp = message + ''.join([' '] * (width - len(message)))
        else:
            temp = ''.join([' '] * (width - len(message))) + message
        res.append('|' + temp + '|')
    res.append(bar)

    return res


if __name__ == '__main__':
    solve()
