#The spreadsheet Kennslumat contains a part of a teaching evaluation
#form. Each line in the spreadsheet is the response of a student to
#the questions given in the header of the document. The question form
#contains a multiple choice question "Hvaða verkefni fannst þér
#skemmtilegust?". Each cell in this question's column contains a comma
#separated list of assignments, which are the choices each student
#made when answering this question.

#In this problem your task is to count the votes of each assignment
#(i.e. how often it was chosen). The spreadsheet will be provided as a
#CSV file. The format of the CSV file can be seen in
#Kennslumat_small.csv. You can also download the whole spreadsheet as
#a CSV file by selecting File > Download as > Comma Separated Values
#(.csv, current sheet).

#Write a function count_votes that takes one parameter, the path to a
#CSV file. The function returns a dictionary, where the keys are the
#names of the assignments and the values are the votes the
#corresponding assignment got in the teaching evaluation.
from collections import Counter
import re
import csv
from pprint import pprint

def count_votes(f):
    dict = {}
    with open(f, newline='', encoding='utf-8') as file:
        data = csv.reader(file)
        lis = list(data)

        for x in lis[1:]:
            votes = list(filter(None, (y.strip() for y in x[3].split(','))))
            for z in votes:
                if z in dict:
                    dict[z] += 1
                else:
                    dict[z] = 1
    return dict


##def count_votes(f):
##    with open(f, encoding='utf-8') as d:
##        r = csv.reader(d)
##        lis = []
##        d = {}
##        for x in r:
##            lis.append(x[3].splitlines())
##        lis[0].pop()
##
##        lis = [x for l in lis for x in l]
##        l = []
##        for x in lis:
##            for y in x.split(', '):
##                l.append(y)
##
##        for x in l:
##            if x in d:
##                d[x] += 1
##            else:
##                d[x] = 1
##
##    return d


print(count_votes('Kennslumat_small.csv'))
##{'10. vika - rafrænt: Leit að mótífum í erfðamengjum': 2,
## '12. vika - rafrænt: Recursive Programming in SML': 2,
## '6. vika - rafrænt: Automata Programming': 1,
## '6. vika - skýrsla: Finite Automata': 1,
## '8. vika - rafrænt: Robots': 2,
## '9. vika - rafrænt: Sets': 1}


##def count_votes(f):
##    with open(f, encoding='utf-8') as d:
##        r = csv.reader(d)
##        d = {}
##        templis = []
##        for x in r:
##            templis.append((x[3].splitlines()))
##                
##        templis[0].pop()
##
##        templis = [item for sublist in templis for item in sublist]
##        lis2 = []
##        for x in templis:
##            for i in x.split(', '):
##                lis2.append(i)
##
##        print(lis2)
##        for x in lis2:
##            if x in d:
##                d[x] += 1
##            else:
##                d[x] = 1
##                
##        return d
