def wordcount(raw_text):
    count = 0
    splitty = raw_text.split()
    for i in splitty:
        count += 1
    return count

raw_text = '1 2 3 4 5 A a A b C d E @ #'

def countcharacters(text):
    dict = {}
    lowercase_text = text.lower()
    for i in list(lowercase_text):
        if i == ' ':
            pass
        elif i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    
    return dict

def test():
    result = countcharacters(raw_text)
    print(result)

test()