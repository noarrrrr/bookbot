def get_book_text(path):
    with open(path) as f:
        content = f.read()
        return content

def wordcount(raw_text):
    count = 0
    splitty = raw_text.split()
    for i in splitty:
        count += 1
    return count

def main():
    num_words = wordcount(get_book_text("books/frankenstein.txt"))
    print(f'Found {num_words} total words')

main()