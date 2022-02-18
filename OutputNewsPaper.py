from typing import List

messages = [["1", "Hello how r u"], ["2", "good ty"],
            ["2", "u"], ["1", "me too bro"]]
width, user_width = 15, 5
"""
splitting:
    process line by line: 
        whenever we need to start a new line, we create a new array
            in user's same dialog, we might need to render them into several lines (how)
            -- current total len = cur word len + total_len: <= user_width:
                arr.extend([current word, ' '])
            ```
            total_len + len(word) <= user_width:
                line = ' '.join([line, word])
                arr.extend([line, ' '])
                i += 1 \\ i increment
            ```
            --                   >              :
                    -- current word len > user_width:
                        separate the word into 2 lines: the exceeded part of word goes back to the array
                    -- current word len < user_wdith, but total_len + curLen > user_width:
                        do not add word to the current line, instead, start a new line
            ```
            if total_len + len(word) > user_width:
                # if total_len takes some space
                if len(word) < user_width:
                    arr.extend([line, ' ']) # append last time's line
                    tmp.append([user_id, arr])
                    arr = []
                    i += 1 \\ i increment
                    
                # word itself too long
                else:
                    if line: 
                        arr.extend([line, ' '])
                    else:
                        \\ cut the word
                        arr.extend(word[:user_width])
                        msg[i] = word[user_width:]
                    tmp.extend([user_id, arr])
                    arr = []
            
            line = '' \\ make line to empty again
            if arr:
                tmp.append([user_id, arr]) \\ squeeze 
            ```
    tag array with user_id (while processing lines)
        
combination:
    +*** .. **+
    render on the right side according to the user_id
"""


def solve():
    res = []
    for message in messages:
        user, msg = message
        arr = msg.split()
        i = 0
        total_len, tmp = 0, []
        line = ''
        while i < len(arr):
            word = arr[i]
            word_len = len(word)
            num_len = total_len + word_len

            if num_len <= user_width:
                line = ' '.join([line, word])
                tmp.extend([line, ' '])
                i += 1

            else:  # we are standing on the i-th word,
                # not because the word itself is too long
                if line:
                    tmp.extend([line, ' '])
                else:
                    # cut the word
                    tmp.extend(word[:user_width])  # the new line only contains part of the word
                    arr[i] = word[user_width:]  # add remaining word back to 'arr'

                res.extend([user, ''.join(tmp).strip()])
                line = ''
                tmp = []

        if len(tmp) > 0:
            res.extend([user, ''.join(tmp).strip()])

    print(res)

    # combination
    for each_line in combination(res, width):
        print(each_line)


"""
+***************+
|Hello          |
|how r          |
|u              |
|           good|
|             ty|
|              u|
|me             |
|too            |
|bro            |
+***************+
"""


def combination(res: List[List[int]], width: int):
    updown = '+' + ''.join(['*'] * width) + '+'
    ret = []
    ret.append(updown)
    for user, sentence in res:
        tmp = ''
        if user == 1:
            tmp = '|' + sentence + ' ' * (width - len(sentence)) + '|'
        else:
            tmp = '|' + ' ' * (width - len(sentence)) + sentence + '|'
        ret.append(tmp)

    ret.append(updown)

    return ret


if __name__ == '__main__':
    solve()
