import os
import math
import xml.etree.ElementTree as ET

def hungry(file, lat, lon):
    tree = ET.parse(file)
    root = tree.getroot()
    lis = []
    for child in root:
        r = child.find('./tag/[@v="restaurant"]')
        f = child.find('./tag/[@v="fast_food"]')
        if r is not None or f is not None:
            lon2 = child.attrib['lon']
            lat2 = child.attrib['lat']
            n = child.find('./tag/[@k="name"]')
            if n is not None:
                name = n.attrib['v']
                dist = (float(lat) - float(lat2))**2 + (float(lon) - float(lon2))**2
                lis.append((dist, name))   
    k = min(lis)
    return k[1]

