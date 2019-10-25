'''
add_bpts_to_found_instructions.py
Description:
    Search inefficiently throughout the file for certain instructions and set breakpoints on all of them
Author: TGZ
Version: 0.0.1
Date: 25 Oct 2019
'''

addr = 0x0
while addr != idc.BADADDR:
   addr = idc.FindText(addr, idc.SEARCH_DOWN | idc.SEARCH_NEXT | idc.SEARCH_REGEX, 0, 0, "call|pop")
   mnem = GetMnem(addr)
   if mnem == "call" or mnem == "pop":
     print "0x%x" % addr
     add_bpt(addr, 0, BPT_SOFT )
   addr = idc.NextHead(addr)
