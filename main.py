from stats import count_words, count_chars

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    path_to_file = "books/frankenstein.txt"
    file_contents = get_book_text(path_to_file)
    count_words(file_contents)
    char_dict = count_chars(file_contents)
    print(char_dict)


if __name__ == "__main__":
    main()
