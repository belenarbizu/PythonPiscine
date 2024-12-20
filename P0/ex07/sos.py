import sys

NESTED_MORSE = {" ": "/ ", "A": ".- ", "B": "-... ", "C": "-.-. ",
                "D": "-.. ", "E": ". ", "F": "..-. ", "G": "--. ",
                "H": ".... ", "I": ".. ", "J": ".--- ", "K": "-.- ",
                "L": ".-.. ", "M": "-- ", "N": "-. ", "O": "--- ",
                "P": ".--. ", "Q": "--.- ", "R": ".-. ", "S": "... ",
                "T": "- ", "U": "..- ", "V": "...- ", "W": ".-- ",
                "X": "-..- ", "Y": "-.-- ", "Z": "--.. ", "1": ".---- ",
                "2": "..--- ", "3": "...-- ", "4": "....- ", "5": "..... ",
                "6": "-.... ", "7": "--... ", "8": "---.. ", "9": "----. ",
                "0": "----- "}


def check_morse(text):
    """
    This function checks if the string is correct and print the morse code
    """
    morse_text = ""
    try:
        for i in range(len(text)):
            try:
                morse_text = morse_text + NESTED_MORSE[text[i].upper()]
            except KeyError:
                raise AssertionError("the arguments are bad")
                sys.exit(1)
        print(morse_text)
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


def main():
    try:
        if (len(sys.argv) != 2):
            raise AssertionError("the arguments are bad")
        else:
            check_morse(sys.argv[1])
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
    main()
