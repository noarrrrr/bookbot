def wordcount(raw_text):
    count = 0
    splitty = raw_text.split()
    for i in splitty:
        count += 1
    return count

test_text = '1 2 3 4 5 A a A b B C d E e e e @ #'

def countcharacters(text):
    dict = {}
    lowercase_text = text.lower()
    for i in list(lowercase_text):
        if i.isalpha():
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
    
    return dict

def sort_key(unsorted_list):
    return unsorted_list['num']

def explode_and_sort(d):
    sorted = []
    for i in d:
        sorted.append({'char': i, 'num': d[i]})
    sorted.sort(reverse=True, key=sort_key)
    return sorted

def test():
    sorted = explode_and_sort(countcharacters(test_text))
    print(sorted)

