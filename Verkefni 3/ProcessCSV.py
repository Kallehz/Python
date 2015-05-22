import re
import csv

def process_csv(f):
    with open(f, encoding='utf-8') as d:
        r = csv.reader(d)
        d = {}
        for x in r:
            n = int(x[2]) * int(x[3])
            if x[0] in d:
                d[x[0]] += n
            else:
                d[x[0]] = n
        
    return d







