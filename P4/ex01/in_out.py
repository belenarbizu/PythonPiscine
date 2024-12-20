

def square(x: int | float) -> int | float:
    return x ** 2


def pow(x: int | float) -> int | float:
    return x ** x


def outer(x: int | float, function) -> object:
    count = 0

    def inner() -> float:
        nonlocal count
        result = x
        for _ in range(count + 1):
            result = function(result)
        count += 1
        return result

    return inner
