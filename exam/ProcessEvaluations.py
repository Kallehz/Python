from collections import Counter
import re
import csv

def count_votes(f):
    with open(f, encoding='utf-8') as d:
        r = csv.reader(d)
        d = {}
        templis = []
        for x in r:
            templis.append((x[3].splitlines()))
                
        templis[0].pop()
        #print(templis)
##        templis = [x for x in templis if x != []]
##
        templis = [item for sublist in templis for item in sublist]
        for x in templis:
            print(','.join(x))

        ## Fæ ekki templis til að verða að einum streng

        print(templis)
##        for x in templis:
##            r = csv.reader(x)
##            print(r)
##        print(Counter(templis))



        

                  
##        for x in templis:
##            if x in d:
##                d[x] += 1
##            else:
##                d[x] = 1
##                
##        return d

print(count_votes('Kennslumat_small.csv'))
##{'10. vika - rafrænt: Leit að mótífum í erfðamengjum': 2,
## '12. vika - rafrænt: Recursive Programming in SML': 2,
## '6. vika - rafrænt: Automata Programming': 1,
## '6. vika - skýrsla: Finite Automata': 1,
## '8. vika - rafrænt: Robots': 2,
## '9. vika - rafrænt: Sets': 1}
