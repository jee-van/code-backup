import json
from difflib import get_close_matches

data = json.load(open('/home/jeevan/python/dictionary/076data.json'))

def dictionary(word):
    similar = get_close_matches(word, data.keys())[0]
    if word in data.keys():
        return data[word]
    elif similar != '':
        print(f"\nDo you mean {similar} instead?")
        yn = input("\nEnter Y for yes and N for no: ").lower()
        if yn == "y":
            return data[similar]
        elif yn == "n":
            return "Invalid word. Please, recheck it."
        else:
            return "We don't understand your input😔 ."
    else:
        return "Invalid word. Please, recheck it."

while True:
    word = input("\nEnter a word OR type X for exit: ").lower()
    if word != "x":
        output = dictionary(word)
        if type(output) == str:
            print(f"\n{output}")
        else:
            print("\n")
            for meanings in output:
                print(meanings)
    else:
        break

