def main() -> str :
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    print(f"Book {book_path} has {get_number_of_words(book_text)} words.")
    print(f"Character count: {get_character_count(book_text)}")

def get_book_text(path) -> str:
    with open(path) as f:
        return f.read()

def get_number_of_words(text) -> int:
    return len(text.split())

def get_character_count(text) -> dict:
    char_count = {}
    lower_text = text.lower()
    for char in lower_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

main()
