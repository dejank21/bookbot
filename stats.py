def get_book_text(path_to_file):
    with open(path_to_file) as file:
        file_contents = file.read()
    return file_contents

def get_num_words(file_contents):
    num_words = file_contents.split()
    return len(num_words)

def times_each_character(text_to_count):
    char_list =  text_to_count.lower()  
    char_count = {}
    for char in char_list:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def characters_sort(times_each_character):
    result = sorted(times_each_character)
    sorted_char = ""
    for char in result:
        if char.isalpha():
            sorted_char += (f"{char}: {times_each_character[char]}\n")
    return sorted_char
        
