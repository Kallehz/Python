import itertools

def longest_common_substring(words):
    sublis = []
    for x in words:
        length = len(x)
        sublis.append([x[i:j+1] for i in range(length) for j in range(i,length)])
    
    #print(sublis)            
    y = set(sublis[0])
    for x in sublis[1:]:
        y.intersection_update(x)
    if len(y) > 0:
        y = max(y, key=len)
        return (len(y))
    return 0;


        
print(longest_common_substring(['lollipop','kiloliters','xylology']))
3
print(longest_common_substring(['hello','hello','helloed']))
##5
print(longest_common_substring(['nooooo','yeeeesss']))
##0

