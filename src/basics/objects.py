

#PROPERTIES
def get_attr_fail_safe(obj,attr):
    if attr in obj.keys():
        return obj[attr]
    else:
        None


def filter_dict_by_dict(dic,filter):
    r=[]
    for entry in dic:
        #when filter empty evertyhing gets selected
        f=True
        for fk, fv in filter.items():
            #filter is found
            if entry.get(fk) == fv:
            #filter key is not found..
                f=True
            else:
                f=False
                break
        if f:
            r.append(entry)
    return r