#!/usr/bin/env python

import requests, json, os, sys, re
from datetime import datetime

def main():
    cbdefense_getevents()

def cbdefense_getevents():
    headers = { 'X-Auth-Token' : os.environ['CBDEFENSE_API'] }
    r = requests.get("https://api-prod05.conferdeploy.net/integrationServices/v3/event?searchWindow=1d&start=1&rows=1000",headers=headers)
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
                            fi.write('[%s] [%s] [%s] \r' % (each['longDescription'], each['eventId'], each['netFlow']['peerFqdn']))
                            fi.close()
                else:
                    pass
            else:
                f = open("carbonblack.log", "a+")
                f.write ('No blocked events as of %s \r' % (datetime.now()))
                f.close()
    else:
        print("oh no, it failed")

if __name__== "__main__":
      main()
