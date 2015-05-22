import re
def css_properties(css):
    p = re.findall(r'([\w|-]+[\s]{0,}):([^;]+)',css)
    return list(tuple(b.strip() for b in a) for a in p)




