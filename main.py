from stats import times_each_character, get_book_text, get_num_words, characters_sort

import sys 

def main():
    text = get_book_text("books/frankenstein.txt")
    char_to_sort = times_each_character(text)
    num_words = get_num_words(text)
    sorted_characters = characters_sort(char_to_sort)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("------- Character Count ---------")
    print(sorted_characters)
    print("============= END ===============")

main()