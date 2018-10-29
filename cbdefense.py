#!/usr/bin/env python
import requests, json, os, sys, re, socket, time
from datetime import datetime
from pandas.io.json import json_normalize

def main():
    cbdefense_getevents()

def cbdefense_getevents():
    headers = { 'X-Auth-Token' : os.environ['CBDEFENSE_API'] }
    r = requests.get("https://api-prod05.conferdeploy.net/integrationServices/v3/event?searchWindow=3h&start=1&rows=2",headers=headers)
    data = r.json()
    if r.status_code == requests.codes.ok:
        for each in data['results']:
            if 'blocked' in each['longDescription']:
                if os.path.isfile("carbonblack.log"):
                    with open('carbonblack.log', 'r+') as fi:
                        text = fi.read()
                        if re.search(each['eventId'], text):
                            fi.close()
                        else:
                            for eventdetails in ['eventId']:
                                event_url="https://api-prod05.conferdeploy.net/integrationServices/v3/event/" + each['eventId']
                                r = requests.get(event_url, headers=headers)
                                resp = r.content
                                if r.status_code == requests.codes.ok:
                                    jj = json.loads(resp)
                                    j = json.dumps(jj)#.replace('\\n','').replace('\\"','"')
                                    fi.write(j + '\r')
                                    fi.close()
                                else:
                                    pass
                else:
                    pass
            else:
                pass
    else:
        print("oh no, it failed")

if __name__== "__main__":
      main()
