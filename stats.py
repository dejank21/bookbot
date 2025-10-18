def get_book_text(path_to_file):
    with open(path_to_file) as file:
        file_contents = file.read().split()
    return file_contents

def get_num_words():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    print(f"Found {len(book_text)} total words")
