def get_word_count(book_text):
    words = book_text.split()
    num_words = len(words)
    return num_words

def get_char_count(book_text):
    char_count = {}
    for character in book_text:
        char = character.lower()
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1

    return char_count

def sort_on(dict):
    return dict["num"]

def char_sort(chars):
    new_list = []
    for item in chars.items():
        new_dict = {
            "char": item[0],
            "num": item[1]
        }
        new_list.append(new_dict)

    new_list.sort(reverse=True, key=sort_on)

    return new_list