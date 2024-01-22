def make_iterable(inp):
    if not isinstance(inp,list):
        return [inp]
    else:
        return inp

def substract_lists(obj,sub):
    return [x for x in obj if not x in sub or sub.remove(x)]