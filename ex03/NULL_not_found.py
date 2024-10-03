def NULL_not_found(object: any) -> int:
    if (object is None):
        print(f"Nothing: {object} <class 'NoneType'>")
        return 0
    elif (isinstance(object, float)):
        print(f"Cheese: {object} <class 'float'>")
        return 0
    elif (isinstance(object, bool)):
        print(f"Fake: {object} <class 'bool'>")
        return 0
    elif (isinstance(object, int)):
        print(f"Zero: {object} <class 'int'>")
        return 0
    elif not object:
        print("Empty: <class 'str'>")
        return 0
    elif (isinstance(object, str)):
        print("Type not Found")
    return 1