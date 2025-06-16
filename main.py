book_path = "/home/nerds/workspace/github.com/ericvalery/bookbot/books/frankenstein.txt"
def get_book_text(book_path):
    with open(book_path) as b:
        book_contents = b.read()
    print(book_contents)
def main():
    return get_book_text(book_path)
main()