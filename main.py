import sys

try:
    PATH = sys.argv[1]
except Exception:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)

def get_book_text(path):
    with open(path) as f:
        content = f.read()
        return content

from stats import wordcount

from stats import countcharacters

from stats import sort_key

from stats import explode_and_sort

def main():
    num_words = wordcount(get_book_text(PATH))
    charcount = explode_and_sort(countcharacters(get_book_text(PATH)))
    
    print(f'''============ BOOKBOT ============
Analyzing book found at {PATH}
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------''')
    for i in charcount:
        print(i['char']+':', i['num'])
    
    
main()