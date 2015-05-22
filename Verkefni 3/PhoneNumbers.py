import urllib.request
import json
import datetime
from pprint import pprint

def companies(day, month, year):
    date = ("{:%d%m%Y}".format(datetime.date(year, month, day)))
    sc = str(int(date[0]) + 4) + date[1:4] + date[6:8]
    url = 'http://apis.is/company?socialnumber=' + sc
    r = urllib.request.urlopen(url).read().decode('utf-8')
    lis = json.loads(r)
    f = []
    for x in lis['results']:
         if x['active']:
            f.append(x['name'])

    return f

