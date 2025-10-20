from stats import times_each_character, get_book_text, get_num_words

def main():
    text_to_count = get_book_text("books/frankenstein.txt")
    print(times_each_character(text_to_count))

main()