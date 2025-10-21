def get_book_text(path_to_file):
    with open(path_to_file) as file:
        file_contents = file.read()
    return file_contents

def get_num_words(file_contents):
    num_words = file_contents.split()
    print(f"Found {len(num_words)} total words")

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
    for character in times_each_character:
        


def print_character_count(times_each_character):
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {get_num_words} total words")
        print("------- Character Count ---------")
        print(characters_sort(times_each_character))
        print("============= END ===============")