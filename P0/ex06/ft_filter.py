def ft_filter(function, iterable):
    """
    This function behaves like the original filter,
    returns an iterator where the items are filtered
    through a function
    """
    return (x for x in iterable if function(x))
