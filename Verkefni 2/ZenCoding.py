# Egill Sveinbjornsson
# Reykjavik University 2015-1

def parse_code(c):
    tuples = {}
    times = 1
    idx = 0
    for b in c.split('>'): # Split by nesting level
        idx += 1
        tuples[idx] = []
        for t in b.split('+'):
            if '*' not in t:
                times = 1
                tuples[idx] += [[t, times]]
            else:
                lis = t.split('*')
                tuples[idx] += [[lis[0], int(lis[1])]]
                times = int(lis[1])
    return [(x, tuples[x]) for x in tuples]

def zen_expand(c):
    s = ''
    blocks = parse_code(c)
    # print(blocks)
    for nesting_level in blocks[::-1]: # Start innermost and work outwards
        tmp = ''
        for i, t in enumerate(nesting_level[1]):
            start_tag = '<' + t[0] + '>'
            end_tag = '</' + t[0] + '>'
            amount = t[1]
            # Check here if its the last tag on this nesting level
            if i == len(nesting_level[1])-1:
                tmp += (start_tag + s + end_tag) * amount
            else:
                tmp += (start_tag + end_tag) * amount
        s = tmp
        # print('Nesting level: ' + str(nesting_level[0]), nesting_level[1])
        # s = s + (tag * amount) + s
    return s

# zen_expand("a+div+p*3>a")
# "<a></a><div></div><p></p><p></p><p></p>"
# zen_expand("dd")
# "<dd></dd>"
# zen_expand("table>tr*3>td*2")
# "<table><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr></table>"
# zen_expand("div*3+p*4+span*2")
# "<div></div><div></div><div></div><p></p><p></p><p></p><p></p><span></span><span></span>"
# zen_expand("table>tr*2>td*2")
# zen_expand('html>head+body>div+div+p>ul>li*3>a')
# "<html><head></head><body><div></div><div></div><p><ul><li><a></a></li><li><a></a></li><li><a></a></li></ul></p></body></html>"