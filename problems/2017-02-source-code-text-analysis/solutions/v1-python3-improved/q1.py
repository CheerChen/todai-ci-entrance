def read_file(filename):
    return open(filename, 'r').read()


content = read_file('data/foo.py')

c_count = 0
w_count = 0
words_list = []
words_dict = {}
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

print(w_count)
print(words_list)
# print sorted(words_dict.items())

# print ' '.lower() in 'abcdefghijklmnopqrstuvwxyz'
