# Program goal, print a list of words delimeted by commas

list_of_words = ["hello", "yes", "goodbye", "last"]

# Method 1

def sortt():
    for i in range(len(list_of_words)):
        if i + 1 < len(list_of_words):
            print(list_of_words[i] + ",", end='')
        else:
            print(list_of_words[i])


# Method 2

def sortt2():
    print(",".join(list_of_words))

# Method 3

def sortt3():
    DELIMETER = ","
    print(DELIMETER.join(list_of_words))

sortt3()