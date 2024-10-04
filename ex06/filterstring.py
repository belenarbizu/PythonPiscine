import sys

def output_list(string, number):
    """
    This function split the string, check if its len is greater than the  and print the list
    """
    words_split = string.split()
    len_word = lambda word: len(word) > number
    output_list = [word for word in words_split if len_word(word)]
    print(output_list)

def check_input(string, number):
    """
    This functions check if the argvs are correct
    """
    if (isinstance(string, str)):
        try:
            num = int(number)
        except:
            print("AssertionError: the arguments are bad")
            sys.exit(1)
        output_list(string, num)
    else:
        print("AssertionError: the arguments are bad")

def main():
    if (len(sys.argv) != 3):
        print("AssertionError: the arguments are bad")
    else:
        check_input(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()