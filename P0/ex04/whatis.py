import sys

def even_or_odd(num):
    if (num % 2 == 0):
        print("I'm Even.")
    else:
        print("I'm Odd.")


def try_argv():
    if (len(sys.argv) > 2):
        print("AssertionError: more than one argument is provided")
    elif (len(sys.argv) == 2):
        try:
            try_int = int(sys.argv[1])
        except:
            print("AssertionError: argument is not an integer")
            sys.exit(1)
        even_or_odd(try_int)
    elif (len(sys.argv) == 0):
        return 0

try_argv()