import re

def jam(string):
    lis = []
    p = re.findall(r',\s(.*),', string)
    for x in p:
        lis.append(x.replace(' with ', ',').replace(' and ' , ',').replace(' plus ' , ',').split(','))
    lis = [item for sublist in lis for item in sublist]
    lis = [i.strip() for i in lis]
    
    d = {}
    for x in lis:
        if x:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1

    return d
