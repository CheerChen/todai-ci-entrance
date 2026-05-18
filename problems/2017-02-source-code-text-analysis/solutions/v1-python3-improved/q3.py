def read_file(filename):
    return open(filename, 'r').read()


content = read_file('data/foo.py')


def get_words_dict(content, words_dict={}):
    c_count = 0
    w_count = 0
    words_list = []
    # words_dict = {}
    word = ''
    for char in content:
        if char.lower() in 'abcdefghijklmnopqrstuvwxyz':
            word += char
            c_count += 1
        else:
            if c_count != 0:
                if word not in words_list:
                    words_list.append(word)
                    words_dict[word] = 1
                    w_count += 1
                else:
                    words_dict[word] += 1
                word = ''
            c_count = 0
    return words_dict


words_dict = get_words_dict(content)

input = input()

order_list = []
if input in words_dict:
    print(input)
else:
    words_dict[input] = 0
    order_list = sorted(words_dict.items())
# print order_list
    for w in order_list:
        if w[0] == input:
            if order_list.index(w) == len(order_list) - 1:
                print('nothing')
            else:
                print(order_list[order_list.index(w) + 1][0])

