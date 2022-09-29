import os
import json
from dotenv import load_dotenv
import sys
from datetime import datetime

print(datetime.now().strftime("%H:%M:%S")+"Executing...")

load_dotenv()
DOMAIN_LIST = json.loads(os.getenv('DOMAIN_LIST'))

if sys.version_info[0] < 3:
    import urllib
    for url in DOMAIN_LIST:
        page = urllib.urlopen(url);
        page.close();
else:
    import urllib.request
    for url in DOMAIN_LIST:
        page = urllib.request.urlopen(url);
        page.close();

print(datetime.now().strftime("%H:%M:%S")+"Done")