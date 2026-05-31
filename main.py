def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def count_words(file_contents):
    words = file_contents.split()
    num_words = len(words)
    msg = f"Found {num_words} total words"
    print(msg)


def main():
    path_to_file = "books/frankenstein.txt"
    file_contents = get_book_text(path_to_file)
    count_words(file_contents)



if __name__ == "__main__":
    main()
