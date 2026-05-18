# create file path list
import os


def read_file(filename):
    return open(filename, 'r').read()


def get_words_dict(content, words_dict):
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


# folders = os.listdir('data/chainer')
# for file in folders:
#     if '.py'
py_list = []
source_suffix = '.py'
dir = 'data'

for root, dirs, files in os.walk(dir):
    # print root,dirs,files
    for file in files:
        if source_suffix in file:
            py_list.append(os.path.join(root, file))


# print len(py_list)

words_dict = {}
for file in py_list:
    content = read_file(file)
    # print len(words_dict)
    words_dict = get_words_dict(content, words_dict)

# del words_dict['descriptor']


def get_top(words_dict):
    max_v = 0
    max_word = ''
    for k, v in words_dict.items():
        if v > max_v:
            max_word = k
            max_v = v
    del words_dict[max_word]
    return max_v, max_word

print get_top(words_dict)
print get_top(words_dict)
print get_top(words_dict)
print get_top(words_dict)
print get_top(words_dict)
print get_top(words_dict)

