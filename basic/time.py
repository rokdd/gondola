from datetime import datetime
import os

from datetime import timedelta

def is_file_older_than (file, delta): 
    cutoff = datetime.utcnow() - delta
    mtime = datetime.utcfromtimestamp(os.path.getmtime(file))
    
    if mtime < cutoff:
        return True
    return False

def all_lists_as_dict(d):
    if isinstance(d, list):
        d={str(o):p for o,p in enumerate(d)}
    for k,v in d.items():
        if isinstance(v, list):
            d[str(k)]={str(o):p for o,p in enumerate(v)}
            v=d[k]
        if isinstance(v, dict):
            all_lists_as_dict(v)
        else:
            pass


def pretty_print_timedelta(t, max_components=None, max_decimal_places=1):
    ''' 
    Print a pretty string for a timedelta. 
    For example datetime.timedelta(days=2, seconds=17280) will be printed as '2 days, 4 hours, 48 minutes'. Setting max_components to e.g. 1 will change this to '2.2 days', where the 
    number of decimal points can also be set. 
    '''
    time_scales = [timedelta(days=365), timedelta(days=1), timedelta(hours=1), timedelta(minutes=1), timedelta(seconds=1), timedelta(microseconds=1000), timedelta(microseconds=1)]
    time_scale_names_dict = {timedelta(days=365): 'year',  
                            timedelta(days=1): 'day', 
                            timedelta(hours=1): 'hour', 
                            timedelta(minutes=1): 'minute', 
                            timedelta(seconds=1): 'second', 
                            timedelta(microseconds=1000): 'millisecond', 
                            timedelta(microseconds=1): 'microsecond'}
    count = 0
    txt = ''
    first = True
    for scale in time_scales:
        if t >= scale: 
            count += 1
            if count == max_components:
                n = t / scale
            else:
                n = int(t / scale)
                
            t -= n*scale
            
            n_txt = str(round(n, max_decimal_places))
            if n_txt[-2:]=='.0': n_txt = n_txt[:-2]
            txt += '{}{} {}{}'.format('' if first else ', ', n_txt, time_scale_names_dict[scale], 's' if n>1 else '', )
            if first:
                first = False

    if len(txt) == 0: 
        txt = 'none'
    return txt
