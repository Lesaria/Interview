'''
Reverse Words in a String
Given an input string, reverse the string word by word.
For example,
Given s = "the sky is blue",
return "blue is sky the".
'''
def revwords(s):
    l=s.split(' ')
    sr = ' '.join(l[::-1])
    return sr
