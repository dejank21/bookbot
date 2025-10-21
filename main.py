from stats import times_each_character, get_book_text, get_num_words, characters_sort

import sys 

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    char_to_sort = times_each_character(text)
    num_words = get_num_words(text)
    sorted_characters = characters_sort(char_to_sort)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("------- Character Count ---------")
    print(sorted_characters)
    print("============= END ===============")

main()