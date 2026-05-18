def edit_distance(word1, word2):
    if len(word1) == 0:
        return len(word2)
    if len(word2) == 0:
        return len(word1)

    if word1 > word2:
        word1, word2 = word2, word1

    dis1 = range(len(word1) + 1)
    dis2 = []
    for i1, c1 in enumerate(word2):
        dis2 = [i1 + 1]
        for i2, c2 in enumerate(word1):
            if c1 == c2:
                dis2.append(dis1[i2])
            else:
                # print c2, dis2[i2], dis1[i2], dis1[i2 + 1]
                dis2.append(1 + min(dis1[i2] + 1, dis1[i2 + 1]))
                # dis2.append(min(dis1[i2] + 2, dis1[i2 + 1] + 1))
        # print dis2
        dis1 = dis2
    return min(dis1[-2] + 1, dis1[-1])


def editDistance(str1, str2, m, n):
    if m == 0:
        return n
    if n == 0:
        return m

    if str1[m - 1] == str2[n - 1]:
        return editDistance(str1, str2, m - 1, n - 1)

    return 1 + min(editDistance(str1, str2, m, n - 1),  # Insert
                   editDistance(str1, str2, m - 1, n - 1) + 1  # Replace
                   )


def read_file(filename):
    return open(filename, 'r').read()


def get_word_list(content):
    c_count = 0
    w_count = 0
    words_list = []
    word = ''
    for char in content:
        if char.lower() in 'abcdefghijklmnopqrstuvwxyz':
            word += char
            c_count += 1
        else:
            if c_count != 0:
                if word not in words_list:
                    words_list.append(word)
                    w_count += 1
                word = ''
            c_count = 0
    return words_list


input = input()
content = read_file('data/foo.py')
word_list = get_word_list(content)

dis = float('+inf')
dis_list = []
for word in word_list:
    if len(input) > len(word):
        dis = float('inf')
    else:
        dis = editDistance(input, word, len(input), len(word))
        # dis = edit_distance(input, word)
    dis_list.append(dis)

min_dis = min(dis_list)
if min_dis == float('inf'):
    print('nothing')
else:
    for k, dis in enumerate(dis_list):
        if dis == min_dis:
            print(word_list[k])

# print editDistance('abcdef', 'ab', 6, 2)
