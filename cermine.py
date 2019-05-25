import requests


def call_cermine(ref_str):
    payload = {'reference': ref_str}

    r = requests.post("http://cermine.ceon.pl/parse.do", params=payload)
    '''print(r.status_code, r.reason)
    print(r.content)'''

    return r.text
