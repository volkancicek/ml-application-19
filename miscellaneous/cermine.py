import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

def call_cermine(ref_str):
    payload = {'reference': ref_str}
    url = "http://cermine.ceon.pl/parse.do"
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    r = session.post(url,data=payload)
    print(r.text)
   # r = requests.post(url, params=payload)
    '''print(r.status_code, r.reason)
    print(r.content)'''

    return r.text
