import pprint
#import logging

#log to file
#success as a status
#cutelog
#colors

def __l_typ__pprint(x,compact=False):
    if isinstance(x,dict):
        return "\n"+pprint.pformat(x,compact=compact)
    
    if type(x).__name__=="DictPath":
        return "\n"+pprint.pformat(x.dict,compact=compact)
    
    return str(x)

def l(*args):
	'''Takes all arguments and join them with a delimiter as string. It simulates like the logging function where you can add multiple arguments which gets concat'''
	return (" ".join([__l_typ__pprint(a) for a in args if not type(a)=="NoneType"]))