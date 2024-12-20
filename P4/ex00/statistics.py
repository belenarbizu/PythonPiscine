

def mean(args):
    if len(args) == 0:
        print("ERROR")
    else:
        sum_arg = 0
        for arg in args:
            sum_arg += arg
        result = sum_arg / len(args)
        print("mean :", result)


def bubbleSort(args):
    sort_num = list(args)
    sorting = True
    while sorting:
        sorting = False
        for i in range(len(sort_num) - 1):
            if sort_num[i] > sort_num[i + 1]:
                sort_num[i], sort_num[i + 1] = sort_num[i + 1], sort_num[i]
                sorting = True
    return tuple(sort_num)


def median(args):
    if len(args) == 0:
        print("ERROR")
    else:
        sorted_num = bubbleSort(args)
        if len(sorted_num) % 2 == 0:
            num_1 = sorted_num[int(len(sorted_num) / 2) - 1]
            num_2 = sorted_num[int(len(sorted_num) / 2)]
            median = (num_1 + num_2) / 2
        else:
            median = sorted_num[int(len(sorted_num) / 2)]
        print("median :", median)


def quartile(args):
    if len(args) == 0:
        print("ERROR")
    else:
        sorted_num = bubbleSort(args)
        quartile = [0.0, 0.0]
        first = len(args) / 4
        last = 3 * len(args) / 4
        quartile[0] = float(sorted_num[int(first)])
        quartile[1] = float(sorted_num[int(last)])
        print("quartile :", quartile)


def std(args):
    if len(args) == 0:
        print("ERROR")
    else:
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
    if len(args) == 0:
        print("ERROR")
    else:
        sum_arg = 0.0
        for arg in args:
            sum_arg += arg
        mean = sum_arg / len(args)
        var = 0.0
        for arg in args:
            var += (arg - mean) ** 2
        var = var / len(args)
        print("var :", var)


def ft_statistics(*args: any, **kwargs: any) -> None:
    stats = ["mean", "median", "quartile", "std", "var"]
    func = {
        "mean": mean,
        "median": median,
        "quartile": quartile,
        "std": std,
        "var": var
    }
    for key in kwargs.values():
        if key in stats:
            func[key](args)
