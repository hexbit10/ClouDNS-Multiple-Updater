import os
import json
from dotenv import load_dotenv
import sys

print("Executing...")
print(os.getenv('DOMAIN_LIST'))

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

print("Done")