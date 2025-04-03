from stats import get_word_count, get_words_count, get_sorted_word_count
import sys

def main():
    print("============ BOOKBOT ============")
    print(len(sys.argv))
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    print(f"Analyzing book found at books/{book_path}...")
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    print("----------- Word Count ----------")
    word_count = get_words_count(text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    print(get_sorted_word_count(word_count))
    print("============= END ===============")

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

main()
