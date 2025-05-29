import hashlib
import json
import sys

def hashMe(msg=""):
    if type(msg) is not str:
        msg = json.dumps(msg,sort_keys=True)  
        
    if sys.version_info.major == 2:
        return str(hashlib.sha256(msg).hexdigest())
    else:
        return hashlib.sha256(str(msg).encode('utf-8')).hexdigest() 