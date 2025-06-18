def get_word_count(book_path):
    num_words = 0
    with open(book_path) as b:
        book_contents = b.read()
    word_list = book_contents.split()
    for word in word_list:
        num_words += 1
    print(f"{num_words} words found in the document")

def get_character_count(book_path):
    char_count_dict = {}
    with open(book_path) as b:
        book_contents = b.read()
    book_contents_low = book_contents.lower()
    for c in book_contents_low:
        if c in char_count_dict:
            char_count_dict[c] += 1
        else:
            char_count_dict[c] = 1

    return char_count_dict

        