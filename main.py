def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    dict_list = convert_list_to_list_dicts(chars_dict)
    sorted_letter_list = sort_letter_list(dict_list)
    print_sorted_letters(book_path, num_words, sorted_letter_list)
    
    


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()

def convert_list_to_list_dicts(chars_dict):
    letterlist = []
    for i in chars_dict:
        if i.isalpha():
            letter = chars_dict[i]
            letterlist.append({"letter": i, "num": letter})
    return letterlist

#
        

def sort_on(dict_item):
    return dict_item['num']

def sort_letter_list(dict_list):
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

def print_sorted_letters(book_path,num_words,sorted_letter_list):  
    print(f"--- Begin report of {book_path} ---\n{num_words} words found in the document\n\n")
    
    for item in sorted_letter_list:
        print(f"The letter '{item['letter']}' was found {item['num']} times")

    print("--- End of report ---")


main()

    

