'''
runTillInstruction.py
Description:
    The script runs the debugger till a particular instruction (e.g. "call", "push").
    In the past when I was thinking of an advanced version of this script it was mainly for generic unpacking purposes, but I'm sure it will come in useful for some other scenarios.
Author: TGZ
Version: 0.0.1
Date: 16 Apr 2019
'''

def getEip():
  rv = idaapi.regval_t()
  idaapi.get_reg_val('EIP',rv)
  return rv.ival

def runTillInstruction(instruction):
  eip = getEip()
  while( GetMnem(eip) != instruction ):
    step_into()
    event = GetDebuggerEvent(WFNE_SUSP, -1)
    eip = getEip()
  
runTillInstruction("call")
