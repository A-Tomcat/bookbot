from stats import get_num_words, get_chars_dict, sort_dict
import sys

def main():
    print("Usage: python3 main.py <path_to_book>")
    #sys.exit(1)
    print(sys.argv)
    book_path = sys.argv[1]
    text = get_book_text(book_path)

    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_list = sort_dict(chars_dict)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        print(f"{item['char']}: {item['num']}")

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()