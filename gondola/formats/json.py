import json

def read(path,default={}):
    """
    read Reads a json file from a path

    _extended_summary_

    Args:
        path (_type_): posix or string path to the file

    Note:
        Default value need to be used when file not exists
    Returns:
        object: json
    """    
    with open(path) as fd:
        config_task = json.load(fd)
        return config_task

def write(path,data):
    with open(path, 'w') as file:
        json.dump(data, file, indent = 4)