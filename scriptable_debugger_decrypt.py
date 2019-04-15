'''
scripted_debug_rename_iat_directory_variables.py
Description:
    The script runs the debugger to perform all steps required to decrypt all strings/functions used by a particular string decryption function.
    When a malware dynamically resolves a new IAT Directory somewhere else, this script renames all variables in the new IAT Directory to the name of where the offsets point to.
    This is to be used while debugging and after entries in a new IAT Directory has been resolved.
Author: TGZ
Version: 0.0.1
Date: 13 Apr 2019
Sample hash: 304115CEF6CC7B81F4409178CD0BCEA2B22FD68CA18DFD5432C623CBBB507154
Example:
    .data:10086C64 dword_10086C64 dd 75AB48C7h
will become:
    .data:10086C64 decrypted_kernel32_LoadLibraryA dd offset kernel32_LoadLibraryA
this will be done for:
    <every other variable in that new IAT Directory>
Usage:
    Modify global variables as required.
    Load the sample, run the script, watch the magic. The script will perform the steps required to dynamically decrypt, rename the strings, then stop after that function.
Note:
    Not all decrypted variables are pointers to functions, so it does not seem like an IAT (unless there is further decryption going on that we missed).
'''

# Global variables
iat_start = 0x10086C60;
iat_end = 0x10086DD4;
call_to_overarching_decryption_function = 0x10002a00;
after_anti_debug = 0x100030e4;
after_call_to_overarching_decryption_function = 0x10002a05;

# Start the debugger at the entry point (working)
run_to(BeginEA());
event = GetDebuggerEvent(WFNE_SUSP, -1)

# Go to the call to overarching decryption function (we can't jump inside the call or else the return will return to the wrong address!)
cpu.eip = call_to_overarching_decryption_function;

# Run till after the anti-debug function and modify the return value
run_to(after_anti_debug);
event = GetDebuggerEvent(WFNE_SUSP, -1)
cpu.eax = 0;
run_to(after_call_to_overarching_decryption_function);
event = GetDebuggerEvent(WFNE_SUSP, -1)

# Now that all our variables are decrypted, rename them
while iat_end >= iat_start:
  current_func_address = read_dbg_dword(iat_start);
  function_name = get_name(current_func_address);
  if(function_name):
    print function_name + " " + hex(current_func_address);   
    set_name(iat_start, "decrypted_"+function_name, flags=0);
  else:
    print "Failed: " + hex(current_func_address) + " " + function_name;
  iat_start += 0x4;

# Our variable/function decryption process is complete, so we close the debugger (optional)
# exit_process();
