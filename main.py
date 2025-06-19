from stats import get_character_count, get_word_count, sorted_dict_list
book_path = "books/frankenstein.txt"

def main():
    print("============ BOOKBOT ============") 
    print(f"Analyzing book found at {book_path}...") 
    print("----------- Word Count ----------")
    print(get_word_count(book_path))
    print("----------Character Count--------")
    the_char_count = get_character_count(book_path)
    new_dict_list = sorted_dict_list(the_char_count)
    for dicts in new_dict_list:
        if dicts["char"].isalpha():
            print(f"{dicts['char']}: {dicts['num']}")
    print("=============END=================")
main()
