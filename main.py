def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    path_to_file = "books/frankenstein.txt"
    file_contents = get_book_text(path_to_file)
    print(file_contents)



if __name__ == "__main__":
    main()
