import sys


def output_list(string, number):
    """
    This function split the string, check if its len is greater
    than the  and print the list
    """
    words_split = string.split()
    def len_word(word): return len(word) > number
    output_list = [word for word in words_split if len_word(word)]
    print(output_list)


def check_input(string, number):
    """
    This functions check if the argvs are correct
    """
    try:
        if (isinstance(string, str)):
            try:
                num = int(number)
            except ValueError:
                raise AssertionError("the arguments are bad")
                sys.exit(1)
            output_list(string, num)
        else:
            raise AssertionError("the arguments are bad")
            sys.exit(1)
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


def main():
    try:
        if (len(sys.argv) != 3):
            raise AssertionError("the arguments are bad")
        else:
            check_input(sys.argv[1], sys.argv[2])
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
    main()
