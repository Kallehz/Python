import os, re
from pprint import pprint

def parse_submissions(d):
    stream = ''
    for root, dirs, files in os.walk(d):
        for f in files:
            if f == 'data.tcl':
                #print(open(os.path.join(root, f), encoding='utf8').read())
                stream += (open(os.path.join(root, f), encoding='utf8').read())


    p = re.findall(r'Problem\s(.*)', stream)
    t = re.findall(r'Team\s(.*)', stream)
    c = re.findall(r'Classify\s(.*)', stream)
    d = re.findall(r'Date\s(.*)', stream)
    lis = list(zip(p,t,c,d))
    lis = sorted(lis, key=lambda x: x[3])
    newLis = []
    for x in lis:
        if x[2] == 'Accepted':
            newLis += [(x[1],x[0])]

    return newLis

