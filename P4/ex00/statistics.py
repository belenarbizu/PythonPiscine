def mean(args):
    sum_arg = 0
    for arg in args:
        sum_arg += arg
    result = sum_arg / len(args)
    print("mean :", result)

def median(args):
    # median
    print("median")

def quartile(args):
    # quartile 25
    # quartile 75
    print("quartile")

def std(args):
    # std
    print("std")

def var(args):
    # var
    print("var")

def ft_statistics(*args: any, **kwargs: any)-> None:
    stats = ["mean", "median", "quartile", "std", "var"]
    func = {
        "mean": mean,
        "median": median,
        "quartile": quartile,
        "std": std,
        "var": var
    }
    if len(args) == 0 or len(kwargs) == 0:
        print("ERROR")
    else:
        for key in kwargs.values():
            if key not in stats:
                print("ERROR")
        for key in kwargs.values():
            if key in stats:
                func[key](args)