input_file = open('test.txt', 'rb')
my_file = input_file.read()

num_lines = len(my_file.splitlines())
num_words = len(my_file.split())
num_chars = len(my_file)

print("Lines: %i\nWords: %i\nCharacters: %i" % (num_lines, num_words, num_chars))

input_file.close()


print('----------------------------------------')


# input_file = open('test.txt', 'r')
# my_file = input_file.read()
#
# for line in my_file:
#     words_list = my_file.split()
#     num_lines = my_file.count('\n') + 1
#     num_words = len(words_list)
#     num_chars = len(my_file)
#
# print("Lines: %i\nWords: %i\nCharacters: %i" % (num_lines, num_words, num_chars))
# input_file.close()
#
# print('----------------------------------------')
#
#
# num_lines = 0
# num_words = 0
# num_chars = 0
#
# with open("test.txt", 'rb') as file:
#     for line in file:
#         words_list = line.split()
#         num_lines += 1
#         num_words += len(words_list)
#         num_chars += len(line)
#
# print("Lines: %i\nWords: %i\nCharacters: %i" % (num_lines, num_words, num_chars))
#
# file.close()
