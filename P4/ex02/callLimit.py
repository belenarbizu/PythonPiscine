def callLimit(limit: int):
    """
    Receives a limit and returns a decorator
    """
    count = 0

    def callLimiter(function):
        """
        Receives a function and returns a wrapper
        """

        def limit_function(*args: any, **kwds: any):
            """
            Wrapper that receives the args.
            Returns the function if the count is lower than the limit.
            Prints an error if the count is bigger than the limit.
            """
            nonlocal count
            count += 1
            if limit >= count:
                return function(*args, **kwds)
            else:
                print(f"Error: {function} call too many times")
        return limit_function
    return callLimiter
