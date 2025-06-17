#!/usr/bin/python3
import sys
from stats import count_words, character_count, get_report

def get_book_text(book):
    with open(book) as f:
        book_text = f.read()
        return book_text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    wc = count_words(text)
    char_count = character_count(text)
    report = get_report(char_count)
    print(f"============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------\nFound {str(wc)} total words\n--------- Character Count -------")
    for dict in report:
        if dict["char"].isalpha():
            print(dict["char"]+": " + str(dict["num"]))
        else:
            pass
    print("============= END ===============")

main()