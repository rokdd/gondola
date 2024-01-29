import json

def read(path,logger):
    with open(path) as fd:
        config_task = json.load(fd)
        #logger.debug(pprint(config_task))
        return config_task

def write(path,data,logger):
    with open(path, 'w') as file:
        json.dump(data, file, indent = 4)