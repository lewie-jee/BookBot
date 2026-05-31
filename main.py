from stats import count_words, count_chars, dict_list

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    path_to_file = "books/frankenstein.txt"
    file_contents = get_book_text(path_to_file)
    print_report(file_contents)

def print_report(file_contents):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    count_words(file_contents)
    print("--------- Character Count -------")
    char_dict = count_chars(file_contents)
    char_dict_list = dict_list(char_dict)
    for char_dict_list_element in char_dict_list:
        if not char_dict_list_element["char"].isalpha():
            continue
        print (f"{char_dict_list_element["char"]}: {char_dict_list_element["num"]}")
    print("============= END ===============")
    




if __name__ == "__main__":
    main()
