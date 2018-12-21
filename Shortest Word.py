'''
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.

'''

def find_short(s):
    s = s.split()
    l = s[0]
    for i in s:
	    if len(i) < len(l):
		    l = i
    return len(l)
