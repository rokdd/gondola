

def filter_items_by_dict(dic,filter,need_all_keys=True):
    r=[]
    for entry in dic:
        #when filter empty evertyhing gets selected
        f=True
        fs=[]
        for fk, fv in filter.items():
            #filter is found
            if entry.get(fk) == fv:
                fs.append(True)
            #filter key is found and value is a list and we found value there
            elif isinstance(entry.get(fk),list) and fv in entry.get(fk):
                fs.append(True)
            #filter key is not found..
            else:
                if need_all_keys:
                    #no need to look further
                    break
        if len(f)>0 and (len(f)==len(filter.keys) or need_all_keys is False):
            #append to the results when at least one result and either all cond True or we dont need all of them to be true
            r.append(entry)
    return r