import numpy as np


def check_error(family):
    """
    This function checks if the argument is a list
    and if it has lists on it
    """
    if not isinstance(family, list):
        raise SystemExit("Error: elements must be a list")
    if not all(isinstance(x, list) for x in family):
        raise SystemExit("Error: elements must be a list")
    list_len = len(family[0])
    for sublist in family:
        if (len(sublist) != list_len):
            raise SystemExit("Error: lists must have the same size")
        for item in sublist:
            try:
                int(item)
            except ValueError:
                raise SystemExit("Error: elements must be ints")


def slice_me(family: list, start: int, end: int) -> list:
    """
    Truncates a new version of the list depending on the start
    and end arguments
    """
    check_error(family)
    a = np.array(family)
    print("My shape is :", a.shape)
    trunc_a = a[start:end]
    print("My new shape is :", trunc_a.shape)
    return trunc_a.tolist()
