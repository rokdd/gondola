def make_iterable(inp):
    """
    make_iterable makes a variable to a list if it is not yet

    Args:
        inp (_type_): variable to convert to list

    Returns:
        list: list, with one or more elements
    """    
    if not isinstance(inp,list):
        return [inp]
    else:
        return inp

def substract_lists(obj:list,sub:list)->list:
    """
    substract_lists removes elements from the first list which are included in the second list

    Args:
        obj (list): list to keep elements
        sub (list): list of elements to remove

    Returns:
        list: shortend list
    """    
    return [x for x in obj if x not in sub or sub.remove(x)]