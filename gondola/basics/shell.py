
from subprocess import check_output, CalledProcessError, STDOUT
import shlex

def system_call(command):
    """ 
    params:
        command: string, ex. `"ls -l"`
    returns: output, success
    """
    command = shlex.split(command)
    try:
        output = check_output(command, stderr=STDOUT).decode()
        success = True 
    except CalledProcessError as e:
        output = e.output.decode()
        success = False
    return output, success

