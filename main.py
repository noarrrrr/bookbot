def get_book_text(path):
    with open(path) as f:
        content = f.read()
        return content

from stats import wordcount

from stats import countcharacters

def main():
    num_words = wordcount(get_book_text("books/frankenstein.txt"))
    charcount = countcharacters(get_book_text("books/frankenstein.txt"))
    print(f'Found {num_words} total words')
    print(charcount)
    
main()