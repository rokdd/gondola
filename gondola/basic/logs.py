import logging

#log to file
#success as a status
#cutelog
#colors


def l(*args):
	'''l Takes all arguments and join them with a delimiter as string. It simulates like the logging function where you can add multiple arguments which gets concat

	:return: concatted string
	:rtype: str
	'''
	return (" ".join(str(a) for a in args))