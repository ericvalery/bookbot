def get_word_count(book_path):
    num_words = 0
    with open(book_path) as b:
        book_contents = b.read()
    word_list = book_contents.split()
    for word in word_list:
        num_words += 1
    return f"{num_words} words found in the document"
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

def sorted_dict_list(unsorted_dict):
    sorted_list = []
    for char in unsorted_dict:
        num = unsorted_dict[char]
        sorted_list.append({"char": char, "num": num})
    sorted_list.sort(key=lambda item: item["num"], reverse=True)
    return sorted_list    
