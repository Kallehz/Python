def birthdays(l):
    d = {}
    x = []
    for s in l.split():
        if s[:4] in d:
            d[s[:4]].append(s)
        else:
            d[s[:4]] = [s]

    for i in d:
        if len(d[i]) > 1:
            x.append(tuple(d[i]))

    print(x)


birthdays('''0212862149
0407792319
0212849289
1112792819
0407992939
0212970299''')