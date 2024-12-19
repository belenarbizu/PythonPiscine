def mean(args):
    sum_arg = 0
    for arg in args:
        sum_arg += arg
    result = sum_arg / len(args)
    print("mean :", result)

def bubbleSort(args):
    sorted_num = list(args)
    sorting = True
    while sorting:
        sorting = False
        for i in range(len(sorted_num) - 1):
            if sorted_num[i] > sorted_num[i + 1]:
                sorted_num[i], sorted_num[i + 1] = sorted_num[i + 1], sorted_num[i]
                sorting = True
    return tuple(sorted_num)

def median(args):
    sorted_num = bubbleSort(args)
    if len(sorted_num) % 2 == 0:
        num_1 = sorted_num[int(len(sorted_num) / 2) - 1]
        num_2 = sorted_num[int(len(sorted_num) / 2)]
        median = (num_1 + num_2) / 2
    else:
        median = sorted_num[int(len(sorted_num) / 2)]
    print("median :", median)

def quartile(args):
    sorted_num = bubbleSort(args)
    quartile = [0.0, 0.0]
    first = len(args) / 4
    last = 3 * len(args) / 4
    quartile[0] = float(sorted_num[int(first)])
    quartile[1] = float(sorted_num[int(last)])
    print("quartile :", quartile)

def std(args):
    sum_arg = 0.0
    for arg in args:
        sum_arg += arg
    mean = sum_arg / len(args)
    std = 0.0
    for arg in args:
        std += (arg - mean) ** 2
    std = (std / len(args)) ** 0.5
    print("std :", std)

def var(args):
    sum_arg = 0.0
    for arg in args:
        sum_arg += arg
    mean = sum_arg / len(args)
    var = 0.0
    for arg in args:
        var += (arg - mean) ** 2
    var = var / len(args)
    print("var :", var)

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