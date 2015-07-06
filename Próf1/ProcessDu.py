#Write a function process_du that takes a string,
#containing the output from a call to du -b.
#The function returns a list of the names of directories (not the full path)
#ordered by size in decreasing #order (largest directory first).
#No test will contain two folders that have the same size.
import re
def process_du(s):
    lis = []
    for du in s.splitlines():
        size = re.findall('(\d+)', du)[0]
        file = re.findall('(\s.+)', du)[0].split('/')
        lis.append((size, file[-1].lstrip()))


    ls = sorted(lis, key=lambda x: int(x[0]), reverse=True)
    l = [x[1] for x in ls]
        
    return l

##def process_du(s):
##    lis = []
##    for du in s.splitlines():
##        size = int(du.split(' ')[0])
##        if du.count('/') > 0:
##            lis.append(tuple((du.split('/')[-1], size)))
##        else:
##            lis.append(tuple((du.split(' ')[-1], size)))
##
##    l = sorted(lis, key=lambda x: x[1], reverse=True)
##    lis2 = []
##    for x in l:
##        lis2.append(x[0])
##    return lis2

print(process_du("""228136 ./Example preim 312
202099  ./Library
561775  ./Submission-arXiv v1
100294  ./B-inv-proposition
799927  ./CodeSage/SageRuns
826594  ./CodeSage
569863  ./Submission-FPSAC2012/Final submission
315957  ./Submission-FPSAC2012/Sample
1210768 ./Submission-FPSAC2012/Galley
6670    ./Submission-FPSAC2012/Original submission/auto
572082  ./Submission-FPSAC2012/Original submission
2737508 ./Submission-FPSAC2012
1298628 ./CodeHaskell/s
4513852 ./CodeHaskell
9759720 ."""))

