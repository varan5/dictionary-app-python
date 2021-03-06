import json
from difflib import get_close_matches
from termcolor import cprint

# text = colored('Hello, World!', 'red')
# print(text)
# cprint('Hello, World!', 'green')

def search_defination():
    dictionary_data = json.load(open('data.json'))
    input_word = input('Enter a word to search its meaning:\t')
    word_to_search = input_word.lower()
    if word_to_search in dictionary_data:
        return dictionary_data[word_to_search]
    elif len(get_close_matches(word_to_search, dictionary_data.keys())) > 0:
        close_match = get_close_matches(word_to_search, dictionary_data.keys(), 8)[0]
        print("Did you mean '%s' instead ?" % close_match)
        print('y/n', end='  ')
        choice = input()
        if choice.lower() == 'y':
            return dictionary_data[close_match]
        else:
            return

    else:
        return


def print_searched_word(searched_defination):
    for item in searched_defination:
        cprint(item, 'blue')






def dictionary_app():
    while True:
        searched_defination = search_defination()
        if searched_defination is not None:
            print_searched_word(searched_defination)
            print()
        else:
            cprint('This is not a word. Please double check it !\n', 'red', 'on_grey')

        search_again_choice = input('Do you want to search again ?  (y/n)  ')
        print()
        if search_again_choice.lower() == 'n':
            break

def main():
    dictionary_app()
main()
