def count_words(file_contents):
    words = file_contents.split()
    num_words = len(words)
    msg = f"Found {num_words} total words"
    print(msg)