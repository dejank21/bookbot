def get_book_text(path_to_file):
    with open(path_to_file) as file:
        file_contents = file.read()
    return file_contents

def get_num_words(file_contents):
    file_contents = file_contents.split()
    print(f"Found {len(file_contents)} total words")

def times_each_character(file_contents):
    char_list = file_contents.split().lower()
    char_count = {}
    for char in char_list:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count