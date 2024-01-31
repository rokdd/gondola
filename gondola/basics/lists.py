def make_iterable(inp):
    if not isinstance(inp,list):
        return [inp]
    else:
        return inp

def substract_lists(obj,sub):
    """
    substract_lists removes elements from the first list which are included in the second list

    _extended_summary_

    Args:
        obj (_type_): list to keep elements
        sub (_type_): lost of elements to remove

    Returns:
        _type_: _description_
    """    
    return [x for x in obj if not x in sub or sub.remove(x)]