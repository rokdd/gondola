

#PROPERTIES
def get_attr_fail_safe(obj,attr):
    if attr in obj.keys():
        return obj[attr]
    else:
        None

