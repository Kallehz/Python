import re
import csv

def process_csv(f):
    with open(f, encoding='utf-8') as d:
        r = csv.reader(d)
        d = {}
        for x in r:
            total = int(x[2]) * int(x[3])
            if x[0] in d:
                d[x[0]] += total
            else:
                d[x[0]] = total

    return d

print(process_csv("process_csv_example_2.txt"))





