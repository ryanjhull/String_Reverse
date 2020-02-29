# This is a simple script to reverse a string, including spaces.

import sys

txt = "welcome to the jungle"

def rev_string(txt):

    chunks = [i for j in txt.split() for i in (j, ' ')][:-1] 
    print(chunks)
    backwards = ''
    count = len(chunks)

    while count > 0:
        word = list(chunks[count-1])
        wcount = len(word)
        while wcount > 0:
            backwards += word[wcount-1]
            wcount -= 1
        count-= 1
    return backwards

if len(sys.argv) > 1:
    txt = str(sys.argv[1])
backwardsStr = rev_string(txt)
print(backwardsStr)
