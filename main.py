from stats import get_character_count, get_word_count
book_path = "/home/nerds/workspace/github.com/ericvalery/bookbot/books/frankenstein.txt"

def get_book_text(book_path):
    with open(book_path) as b:
        book_contents = b.read()
    print(book_contents)

def main():
    the_char_count = get_character_count(book_path)
    print(get_word_count(book_path), the_char_count )
    
main()