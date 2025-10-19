def get_word_count(text) -> int:
    return len(text.split())

def get_character_count(text) -> dict:
    char_count = {}
    lower_text = text.lower()
    for char in lower_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def get_dict_count(dict):
    return dict['count']

def get_sorted_char_list(dict) -> list:
    sorted_list = []

    for k,v in dict.items():
        char_dict = {}
        char_dict['char'] = k
        char_dict['count'] = v
        sorted_list.append(char_dict)

    sorted_list.sort(reverse=True, key=get_dict_count)
    return sorted_list



