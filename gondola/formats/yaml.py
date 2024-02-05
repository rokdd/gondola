import yaml
import os
def read(path,default={}):
    """
    read Reads a yaml file from a path

    _extended_summary_

    Args:
        path (_type_): posix or string path to the file

    .. todo:: Default value need to be used when file not exists

    Returns:
        object: dict
    """    
    

    if os.path.exists(path):
        with open(path) as fd:

            mapping = yaml.safe_load(fd)
            return mapping
    return default