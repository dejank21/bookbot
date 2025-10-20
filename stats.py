def get_book_text(path_to_file):
    with open(path_to_file) as file:
        file_contents = file.read()
    return file_contents

def get_num_words(file_contents):
    num_words = file_contents.split()
    print(f"Found {len(num_words)} total words")

def times_each_character(get_book_text):
    char_list =  get_book_text.split().lower()  
    char_count = {}
    for char in char_list:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count