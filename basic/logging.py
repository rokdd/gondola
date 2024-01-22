import logging

GONDOLA_LOGGING_USE_SUCCESS=False

#ADD A NEW STATUS FOR LOGGING ALSO SUCCESS
SUCCESS = 5
logging.addLevelName(5, 'SUCCESS')
setattr(logging, 'SUCCESS', 5)


from logging.handlers import SocketHandler


formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
logging.propagate = False
import pprint

# COLORS taen from here: https://gist.github.com/hosackm/654d64760e979280e6fb431af999f489

from colorama import init, Fore, Back
init(autoreset=True)
class ColorFormatter(logging.Formatter):
    
    # Change this dictionary to suit your coloring needs!
    COLORS = {
        "WARNING": Fore.RED,
        "ERROR": Fore.RED + Back.WHITE,
        "DEBUG": Fore.BLUE,
        "INFO": Fore.GREEN,
        "CRITICAL": Fore.RED + Back.WHITE,
        "SUCCESS": Fore.GREEN
    }

    def format(self, record):
        color = self.COLORS.get(record.levelname, "")
        if color:
            record.name = color + record.name
            record.levelname = color + record.levelname
            record.msg = l(record.msg)
        return logging.Formatter.format(self, record)

#our own logging class
class Logger(logging.Logger):
    super(logging.Logger)
    def __init__(self, name):
        logging.Logger.__init__(self, name)
     
	 	#first time we call.. time to initiate some actions, which we only want to initate once
        if len(self.handlers)==0:
			#console
            color_formatter = ColorFormatter("%(name)-10s %(levelname)-10s %(message)s")
            console = logging.StreamHandler()
            console.setFormatter(color_formatter)
            self.addHandler(console)
            self.propagate = 1
        self.setLevel(logging.SUCCESS)

    def success(self, msg, *args, **kwargs):
        if self.isEnabledFor(SUCCESS):
            self._log(SUCCESS, msg, args, **kwargs)

    def sub_logger(self,name, log_file, level=logging.DEBUG,folder="./"):
        """To setup as many loggers as you want"""
        file_handler = logging.FileHandler(folder+log_file,mode='a')
        color_formatter = logging.Formatter("%(name)-10s %(levelname)-10s %(message)s")
        file_handler.setFormatter(color_formatter)
      
        self.getChild(name).addHandler(file_handler)
        #color_formatter = ColorFormatter("%(name)-10s %(levelname)-18s %(message)s")
        #console = logging.StreamHandler()
        #console.setFormatter(color_formatter)
        #logger_main.getChild(name).addHandler(color_formatter)
        setattr(self.getChild(name),"propagate",False)
        return self.getChild(name)

#this is the default now
logging.setLoggerClass(Logger)

#log to file
#success as a status
#cutelog
#colors

##pprint verwenden
def __l_typ__pprint(x,compact=False):
    if isinstance(x,dict):
        return "\n"+pprint.pformat(x,compact=compact)
    
    if type(x).__name__=="DictPath":
        return "\n"+pprint.pformat(x.dict,compact=compact)
    
    return str(x)

def l(*args):
	'''Takes all arguments and join them with a delimiter as string. It simulates like the logging function where you can add multiple arguments which gets concat'''
	return (" ".join([__l_typ__pprint(a) for a in args if not type(x)=="NoneType"]))

'''


from logging.handlers import SocketHandler
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
logging.propagate = False



# first file logger
lg={}
logger = logging.getLogger("fdk-migrate")
if len(logger.handlers)==0:
    handler=SocketHandler('127.0.0.1', 19996)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    lg[GENERAL_LOGGER] = setup_logger('general', 'general.log')

    
def print_info(message,handler):
    return print_log(message,handler,typ="info")

def print_log(message,handler,typ="info"):
    #https://pypi.org/project/colored/
    colors={"debug":"grey","warn":"magenta","error":"red","info":"blue"}
    colored(message,colors[typ])
    getattr(globals()["lg"][handler],typ)(message)
'''