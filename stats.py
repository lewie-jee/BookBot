from typing import TypedDict

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

class CharacterCount(TypedDict):
    char: str
    num: int

def sort_on(char_dict_list_element):
    return char_dict_list_element["num"]

def dict_list(char_dict: dict) -> list[CharacterCount]:
    char_dict_list = list()
    for char_element in char_dict:
        char_dict_list_element = dict()
        char_dict_list_element["char"] = char_element
        char_dict_list_element["num"] = char_dict[char_element]
        char_dict_list.append(char_dict_list_element)
    char_dict_list.sort(reverse = True, key = sort_on)
    return char_dict_list
    
