'''
runToUserCode.py
Description:
    This code assumes that user code is anything below 0x70000000 (there's actually an exact more accurate number which I forgot...).
    It is similar to setting breakpoints on other segments and then pressing F9 I guess, just that we are scripting it here.
    While EIP is inside system code, it will continuously try to run and return until it hits user code.
Author: TGZ
Version: 0.0.1
Date: 16 Apr 2019
'''

def runToUserCode():
  rv = idaapi.regval_t()
  idaapi.get_reg_val('EIP',rv)
  ea = rv.ival
  while(ea>0x70000000):
    step_until_ret();
    break;
    
runToUserCode();
