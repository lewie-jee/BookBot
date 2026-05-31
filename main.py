from stats import count_words, count_chars, dict_list
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1] 
    file_contents = get_book_text(path_to_file)
    print_report(path_to_file, file_contents)

def print_report(path_to_file, file_contents):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    count_words(file_contents)
    print("--------- Character Count -------")
    char_dict = count_chars(file_contents)
    char_dict_list = dict_list(char_dict)
    for char_dict_list_element in char_dict_list:
        if not char_dict_list_element["char"].isalpha():
            continue
        print (f"{char_dict_list_element['char']}: {char_dict_list_element['num']}")
    print("============= END ===============")
    




if __name__ == "__main__":
    main()
