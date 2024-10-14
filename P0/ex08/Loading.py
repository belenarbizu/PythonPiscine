def ft_tqdm(lst: range) -> None:
    """
    This function behaves like the original tqdm function
    """
    lenght = 143
    last = lst[-1] + 1
    for i in lst:
        percentage = i * 100 / last
        bar_lenght = int(i / last * lenght)
        bar = "=" * bar_lenght
        if (i == lst[-1]):
            bar += ">]"
        print(f"\r{percentage:.0f}%|[{bar}| {i + 1}/{last}", end="")
        yield i
