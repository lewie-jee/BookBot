def count_words(file_contents):
    words = file_contents.split()
    num_words = len(words)
    msg = f"Found {num_words} total words"
    print(msg)

def count_chars(file_contents):
    char_dict = dict()
    for char in file_contents:
        char = char.lower()
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict