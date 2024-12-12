import numpy as np


def bmi_form(height, weight) -> int | float:
    """
    This is the bmi formula
    """
    return (np.array(weight) / np.array(height) ** 2)


def check_error(height: list[int | float], weight: list[int | float]):
    """
    Check if lists are correct
    """
    if (len(height) != len(weight)):
        raise SystemExit("Error: lists have to be the same size")
    if not (all(isinstance(x, (int, float)) for x in height)
            and all(isinstance(x, (int, float)) for x in weight)):
        raise SystemExit("Error: elements must be int or float")


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    Creates the list with the bmi data and return it
    """
    check_error(height, weight)
    return bmi_form(height, weight).tolist()


def check_error_limit(bmi: list[int | float]):
    """
    Check int and float error for the bmi list
    """
    if not all(isinstance(x, (int, float)) for x in bmi):
        raise SystemExit("Error: elements must be int or float")


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    This function returns a bool list compairing the limit
    with each member of the bmi list
    """
    check_error_limit(bmi)
    limit_list = []
    for value in bmi:
        limit_list.append(True) if value > limit else limit_list.append(False)
    return limit_list
