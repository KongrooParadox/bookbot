def main() -> str :
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    print(get_number_of_words(book_text))


def get_book_text(path) -> str:
    with open(path) as f:
        return f.read()

def get_number_of_words(text) -> int:
    return len(text.split())

main()
