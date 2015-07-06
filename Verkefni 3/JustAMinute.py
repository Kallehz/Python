import re

def jam(string):
    lis = []
    p = re.findall(r',\s(.*),', string)
    for x in p:
        lis.append(x.replace(' with ',',').replace(' and ',',').replace(' plus ',',').split(','))
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

print(jam("""1/1/1 22 December 1967, Nicholas Parsons with Derek Nimmo, Clement Freud, Wilma Ewart and Beryl Reid, excuses for being late.
2/1/2 29 December 1967, Nicholas Parsons with Derek Nimmo, Clement Freud, Sheila Hancock and Carol Binstead, bedrooms.
3/1/3 5 January 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Betty Marsden and Elisabeth Beresford, ?
4/1/4 12 January 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Isobel Barnett and Bettine Le Beau, ?
5/1/5 20 January 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Andree Melly and Prunella Scales, the brownies
6/1/6 27 January 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Marjorie Proops and Millie Small, ?
7/1/7 2 February 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Aimi Macdonald and Una Stubbs, my honeymoon.
8/1/8 9 February 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Lucy Bartlett and Anona Winn, bloomer.
9/1/9 17 February 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Andree Melly and Charmian Innes, ?
10/1/10 23 February 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Barbara Blake and Renee Houston, my first grown-up dress."""))
##{'Aimi Macdonald': 1,
## 'Andree Melly': 2,
## 'Anona Winn': 1,
## 'Barbara Blake': 1,
## 'Beryl Reid': 1,
## 'Bettine Le Beau': 1,
## 'Betty Marsden': 1,
## 'Carol Binstead': 1,
## 'Charmian Innes': 1,
## 'Clement Freud': 10,
## 'Derek Nimmo': 10,
## 'Elisabeth Beresford': 1,
## 'Isobel Barnett': 1,
## 'Lucy Bartlett': 1,
## 'Marjorie Proops': 1,
## 'Millie Small': 1,
## 'Nicholas Parsons': 10,
## 'Prunella Scales': 1,
## 'Renee Houston': 1,
## 'Sheila Hancock': 1,
## 'Una Stubbs': 1,
## 'Wilma Ewart': 1}
