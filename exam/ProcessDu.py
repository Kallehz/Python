def process_du(s):
    for du in s.splitlines():
        print(du)



##    lis2 = []
##    for x in lis:
##        lis2.append(x.split('.')[1:])
##
##    for x in lis2:
##        print(x)


print(process_du("""
228136 ./Example preim 312
202099  ./Library
561775  ./Submission-arXiv v1
100294  ./B-inv-proposition
799927  ./CodeSage/SageRuns
826594  ./CodeSage
569863  ./Submission-FPSAC2012/Final submission
315957  ./Submission-FPSAC2012/Sample
1210768 ./Submission-FPS
AC2012/Galley
6670    ./Submission-FPSAC2012/Original submission/auto
572082  ./Submission-FPSAC2012/Original submission
2737508 ./Submission-FPSAC2012
1298628 ./CodeHaskell/s
4513852 ./CodeHaskell
9759720 .
"""))

##['.', 'CodeHaskell', 'Submission-FPSAC2012', 's', 'Galley', 'CodeSage', 'SageRuns',
## 'Original submission', 'Final submission', 'Submission-arXiv v1', 'Sample',
## 'Example preim 312', 'Library', 'B-inv-proposition', 'auto']


##    l = [' '.join(x.split()) for x in s.splitlines()]
##    l = [x.split(' ', 8) for x in l if x[0] != 'd']
##    l = sorted(l, key=lambda x: x[8], reverse=True)
##    l = sorted(l, key=lambda x: int(x[4]))
##    n = []
##    for x in l:
##        n.insert(0, x[8])
##           
##    return n
