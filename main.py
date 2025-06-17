from stats import count_words

def get_book_text(book):
    with open("books/" + book) as f:
        book_text = f.read()
        return book_text

def main():
    text = get_book_text("frankenstein.txt")
    wc = count_words(text)
    print(str(wc) + " words found in the document")

main()