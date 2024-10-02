def all_thing_is_obj(object: any) -> int:
    if (isinstance(object, list)):
        print("")
    elif (isinstance(object, tuple)):
        print("")
    elif (isinstance(object, set)):
        print("")
    elif (isinstance(object, dict)):
        print("")
    elif (isinstance(object, str)):
        print("")
    elif (isinstance(object, int)):
        print("Type not found")
    return 42