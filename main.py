from stats import get_character_count, get_word_count, get_sorted_char_list
import sys

def main() -> str :
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        print("Please provide book path !")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    book_word_count = get_word_count(book_text)
    book_character_count = get_character_count(book_text)
    book_sorted_character_count = get_sorted_char_list(book_character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {book_word_count} total words")
    print("--------- Character Count -------")
    for i in book_sorted_character_count:
        if i['char'].isalpha():
            print(f"{i['char']}: {i['count']}")
    print("============= END ===============")

def get_book_text(path) -> str:
    with open(path) as f:
        return f.read()

main()
