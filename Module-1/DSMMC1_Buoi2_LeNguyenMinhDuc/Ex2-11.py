def find_longest_word(input_str):
    words = input_str.split()
    longest_word = max(words, key=len)
    return longest_word

def find_word_position(input_str, word):
    words = input_str.split()
    try:
        position = words.index(word)
    except ValueError:
        position = -1
    return position + 1

input_str = input("Nhap xau ky tu: ")

longest_word = find_longest_word(input_str)
print("Tu dai nhat la:", longest_word)

word_position = find_word_position(input_str, longest_word)
if word_position != -1:
    print("Tu do xuat hien o vi tri:", word_position)
