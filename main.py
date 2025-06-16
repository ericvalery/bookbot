book_path = "/home/nerds/workspace/github.com/ericvalery/bookbot/books/frankenstein.txt"

def get_book_text(book_path):
    with open(book_path) as b:
        book_contents = b.read()
    print(book_contents)
def get_word_count(book_path):
    num_words = 0
    with open(book_path) as b:
        book_contents = b.read()
    word_list = book_contents.split()
    for word in word_list:
        num_words += 1
    print(f"{num_words} words found in the document")
def main():
   return get_word_count(book_path) 
    
main()