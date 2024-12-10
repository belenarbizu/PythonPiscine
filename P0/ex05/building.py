import sys


def print_text(char):
    """
    This function will print the output
    """
    print(f"The text contains {char[0]} characters:")
    print(f"{char[1]} upper letters")
    print(f"{char[2]} lower letters")
    print(f"{char[3]} punctuation marks")
    print(f"{char[4]} spaces")
    print(f"{char[5]} digits")
    pass


def count_char(text):
    """
    This function counts the characters
    """
    characters = []
    characters.append(len(text))
    for i in range(1, 6):
        characters.append(0)
    for i in range(0, len(text)):
        code = ord(text[i])
        if code >= 65 and code <= 90:
            characters[1] += 1
        elif code >= 97 and code <= 122:
            characters[2] += 1
        elif code >= 33 and code <= 47:
            characters[3] += 1
        elif text[i] in " \t\n\r":
            characters[4] += 1
        elif code >= 48 and code <= 57:
            characters[5] += 1
        else:
            print (f"Unrecognized character {code}")
    print_text(characters)
    pass


def main():
    try:
        if (len(sys.argv) < 2):
            sys.stdout.write("What is the text to count?\n")
            sys.stdout.flush()
            text = sys.stdin.readline()
            count_char(text)
        elif (len(sys.argv) > 2):
            raise AssertionError("more than one argument is provided")
        else:
            count_char(sys.argv[1])
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
    main()
