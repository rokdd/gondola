'''

import requests
import app.settings as settings

http = requests.Session()

from requests.adapters import HTTPAdapter
import requests
import urllib

DEFAULT_TIMEOUT = 60 # seconds

class TimeoutHTTPAdapter(HTTPAdapter):
    def __init__(self, *args, **kwargs):
        self.timeout = DEFAULT_TIMEOUT
        if "timeout" in kwargs:
            self.timeout = kwargs["timeout"]
            del kwargs["timeout"]
        super().__init__(*args, **kwargs)

    def send(self, request, **kwargs):
        timeout = kwargs.get("timeout")
        if timeout is None:
            kwargs["timeout"] = self.timeout
        if "?hh" in request.url:
            print(request.url)
            main, querystr = request.url.split('?') # Nasty hack, not always valid.
            print(querystr)
            querystr = urllib.parse.unquote(querystr)
            print(querystr)
            querystr = urllib.parse.quote(querystr, safe='/&:=[]')
            request.url = '?'.join([main, querystr])
            print(querystr)
            print(request.url)
        
        return super().send(request, **kwargs)
   
from requests.packages.urllib3.util.retry import Retry

        

retry_strategy = Retry(
    total=20,
    status_forcelist=[429, 500, 502, 503, 504],
    method_whitelist=["HEAD", "GET", "OPTIONS"]
)


# Mount it for both http and https usage
adapter = TimeoutHTTPAdapter(timeout=50,max_retries=retry_strategy)
http.mount("https://", adapter)
http.mount("http://", adapter)


from urllib.request import urlopen

def req(url,method="get",return_obj=False,return_json=True,**kwargs):
    foo = kwargs.pop('headers') if "headers" in kwargs.keys() else {}
    #print(url)
    q=""

    if "params" in kwargs.keys():
        if "filter" in kwargs["params"].keys() and not isinstance(kwargs["params"]["filter"],str):
            kwargs["params"]["filter"]=json.dumps(kwargs["params"]["filter"])
        kwargs["params"]= "&".join("%s=%s" % (k,v) for k,v in kwargs["params"].items())
        settings.lg["g"].debug("Changed params query:"+kwargs["params"])
        q="?"+kwargs["params"]
        kwargs.pop('params')
    

    response = getattr(http,method)((settings.base_url if not "http" in url else "")+url+q, headers={**settings.headersAPI  ,**foo} if not "http" in url else foo, verify=True,**kwargs)
    if "data" in kwargs.keys():
        kwargs.pop("data")
    settings.lg["g"].debug(settings.l(method,":",url,foo),extra={"response":response.text,"headers:":{**settings.headersAPI,**foo}if not "http" in url else foo,**kwargs})
    if not return_json:
        return response
    if response.text=="":
        if return_obj:
            return response,{}
        return {}
    if return_obj:
        return response,response.json()
    return response.json()
'''