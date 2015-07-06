# Grep
#
# Grep is a command-line utility used for searching plain-text data for lines matching a regular expression.
# Your task is to write a function in Python that serves a similar purpose.
#
# Write a function grep that takes two parameters, the path to a directory and a string containing a valid regular expression.
# The function returns a list of the occurrences of the pattern in the lines of the files in the specified directory,
# or any of its subdirectories. The search for patterns should be done on a line to line basis
# (you should not search for patterns over multiple lines).
# Each occurrence (i.e. element in the list) is represented by a pair (2-tuple).
# The first element of the tuple contains the name of the file of the occurrence,
# and the second element contains the line of the occurrence.

import re
import os


def grep(directory, regx):
    stream = ''
    pathlist = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            # extlist.append(f.split('.')[-1])
            # if f in extlist:
            #     stream += (open(os.path.join(root, f), encoding='utf8').read())
            pathlist.append(os.path.join(root, f))
        print(pathlist)
    for filepath in pathlist:
        file = open(filepath, encoding="utf8")
        print(file)







grep('templates', '<student>')
# [('exam.xml', '\t<student>'), ('exam.xml', '\t<student>')]
