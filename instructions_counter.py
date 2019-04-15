'''
instructions_counter.py
Description:
    The script counts the number of instructions at a particular function and prints it out.
    It gets the current function based on wherever the IDA cursor is (works on both disassembly or decompiler - can be in the middle of the function).
Author: Chris Eagle
Note:
    Basically a slightly modified script from Chris Eagle's IDA Pro book.
'''

func = get_func(here()) # here() is synonymous with ScreenEA()
if not func is None:
  fname = Name(func.startEA)
  count = 0

for i in FuncItems(func.startEA):
  count = count + 1
print "%s contains %d instructions\n" % (fname,count)
