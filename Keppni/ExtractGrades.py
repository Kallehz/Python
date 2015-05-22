from re import match as m
from re import sub as p
from re import findall as f

def extract(s):
    z = []
    l = []
    for x in p(r'[-,.\'\\\s]', '', s).replace('l', '1').replace('O', '0'):
        z.append(x)
    for i in range(1,len(z)):
        if z[i-1] is '1' and z[i] is '0':
            z[i-1] = '10'
            z[i] = ''
    for x in list(filter(None, z)):
        if x.isdigit() and ((int(x) >= 4 or int(x) >= 10)):
            l.append(x)
        elif m('[MSms]+', x):
            l += x.upper()
        else:
            return None

    return l

##    s = p('\W', '', s)
##    s = p('l', '1', s)
##    s = p('O', '0', s.upper)
##    s = f('[MS][4-9][10]', s)
##    if ''.join(s) == lis:
##        return lis

