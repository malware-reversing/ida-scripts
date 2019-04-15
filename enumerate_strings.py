
'''
enumerate_strings.py
Description:
    Slightly modified script to enumerate all strings and respective addresses of certain string types in a file
Author: Elias Bachaalany @ https://github.com/orgs/idapython
Note:
    Enumerating strings based on https://github.com/idapython/src/blob/master/examples/ex_strings.py
'''

s = Strings()
s.setup(strtypes=[STRTYPE_C, STRTYPE_C_16])
for i, v in enumerate(s):
  print str(hex(v.ea)) + ": " + str(v)
