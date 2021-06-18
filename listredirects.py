#!/usr/bin/env python3

import requests
from sys import argv

if(len(argv) == 1):
    print("Usage: python3 listaredirects.py <url>")
    exit(1)

else:
    c = 1
    if("https://" in argv[1] or "http://" in argv[1]):
        pass
    else:
        argv[1] = "http://" + str(argv[1])
    r = requests.get(argv[1])
    for i in r.history:
        print(str(c) + " ---->  " + str(i.url[0:60]) + "...")
        c += 1
    print(str(c) + " ---->  " + str(r.url[0:60]) + "...")
